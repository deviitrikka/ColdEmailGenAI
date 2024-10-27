import pandas as pd
import chromadb
import uuid
import os
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

class Portfolio:
    def __init__(self, file_name = "my_portfolio.csv"):
        self.file_path = os.path.join(os.path.dirname(__file__), "resources", file_name)
        self.df = pd.read_csv(self.file_path)
        self.client = chromadb.PersistentClient('vectorstore')
        self.collection = self.client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):

        if not self.collection.count():
            for _, row in self.df.iterrows():
                self.collection.add(documents = row["Techstack"],
                            metadatas={"links": row["Links"]},
                            ids=[str(uuid.uuid4())])
                
    def query_links(self, skills):
        return self.collection.query(query_texts=skills, n_results=2).get('metadatas',[])
