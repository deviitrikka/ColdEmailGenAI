import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            temperature = 0,
            # groq_api_key = os.getenv("groq_api_key"),
            groq_api_key = st.secrets["api_key"],
            model_name="llama-3.1-70b-versatile"
        )

    def extract_jobs(self,cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`,`skills`,`experience`,`job_details`
            Only return the valid json.
            ### VALID JSON (NO PREAMBLE) :
            """
        )
        chain = prompt_extract | self.llm #chain in langchain
        response = chain.invoke(input={'page_data':cleaned_text})

        try:
            response = JsonOutputParser().parse(response.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return response if isinstance(response,list) else [response]
    
    def write_email(self,job,links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are Mohini, a business development executive at Tinfosys. Tinfosys is an AI & Software Company.
            the seamless integration of business processes through automated tools.
            Over our experience, we have empowered numerous enterprises with tailored solutions, process optimization,cost reduction, and heightened overall efficiency.
            Your job is to write a cold email to the client regarding the job mentioned above in fulfulling their needs.
            Also add the most relevant ones from the following links to showcase Tinfosys's portfolio.
            Remember you are Mohini, BDE at Tinfosys.
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):
            """
        )

        chain_email = prompt_email | self.llm
        email = chain_email.invoke({"job_description":str(job),"link_list": links})
        return email.content
    
if __name__ == "__main__":
    print(st.secrets["api_key"])
