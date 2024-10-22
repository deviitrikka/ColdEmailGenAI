# Cold Email Generator 🚀

An end-to-end generative AI solution designed for sales teams in large software service companies like TCS, Infosys, and STC. This project automates the generation of cold emails by scraping job portals for required skills and job details, then leveraging an LLM (GroqCloud API) to create targeted cold emails for potential clients.

## Problem Statement ❓

In software service companies with massive engineering staff (like TCS, Infosys, etc.), sales teams often reach out to potential clients (Nike, JPMorgan, Adidas) offering specialized services. To streamline this process, sales teams traditionally review job portals to find relevant requirements (e.g., skills needed for roles like AI/ML Developer) and then craft cold emails based on those findings.

This project automates this entire workflow:
- Scrapes job portals to extract the required skills and job descriptions.
- Uses a generative AI model (LLM) to craft personalized cold emails.
- Enables sales teams to efficiently reach out to potential clients without manually sifting through job postings.

## Scope 🌐
1. Scrape job portal URLs to fetch job descriptions, skills, and relevant data.
2. Automatically generate cold emails tailored to the client’s hiring needs using the GroqCloud API.
3. Provide a dashboard to monitor scraped data and generated emails.
4. Useful for sales teams in software consulting firms to pitch contract-based hiring solutions to companies.

## Tech Stack 🛠️

<details> <summary>UI</summary>
<ul>
<li><a href="https://streamlit.io/">Streamlit</a></li>
<li><a href="https://www.python.org/">Python</a></li>
</ul>
</details>

<details> <summary>Database</summary>
<ul>
<li><a href="https://www.trychroma.com/">Chroma DB</a></li>
</ul>
</details>

<details> <summary>Modules & API</summary>
<ul>
<li><a href="https://pandas.pydata.org/">pandas</a> (Data Manipulation)</li>
<li><a href="https://console.groq.com/">GroqCloud API</a> (LLM for Email Generation)</li>
</ul>
</details>

## Features ⚙️

### User Functions:
- Input a job portal URL for scraping (e.g., LinkedIn, Indeed).
- Automatically extract job requirements and descriptions.
- Generate personalized cold emails based on job data using LLM.
- Export generated emails in a user-friendly format (PDF/HTML).

### Admin Functions:
- Monitor the scraping and email generation process.
- View client interaction logs.
- Download email generation reports for internal use.

## Requirements 📋

- Python 3.10+
- GroqCloud API key
- Chroma DB (Vector database)

## Setup & Installation 🚀

```bash
# Clone the repository
git clone https://github.com/your-username/Cold-Email-Generator.git
cd Cold-Email-Generator

# Create and activate a virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install required packages
pip install -r requirements.txt

# Set up the Django app and SQLite database
python manage.py migrate

# Configure GroqCloud API in settings.py

# Start the web app
python manage.py runserver
```
# Known Issues 🚧

- Ensure the WebDriver matches your browser version to avoid compatibility errors.
- A stable internet connection is required for GroqCloud API calls.
S- ome job portals may have scraping limitations (e.g., CAPTCHA).
# Usage 🎯
- Navigate to the dashboard after launching the app.
- Enter a job portal URL (e.g., LinkedIn job page).
- Click "Scrape" to fetch job description and required skills.
- Generate a cold email using the "Generate Email" button.

# Contributing 🤝
Contributions are welcome! Please follow these steps for contributing:
```bash
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -m 'Add feature').
Push to the branch (git push origin feature-branch).
Open a pull request for review.
```
# Preview 👀
![image](https://github.com/user-attachments/assets/59ad8558-ca7a-413c-9511-4bb7a0a04776)


# Acknowledgements 🎉
GroqCloud API for LLM-based email generation.
Langchain documentation for scraping tutorials.
Mr. Dhaval Patel for guidance and project assistance.
# License 📄
This project is licensed under the MIT License. See the LICENSE file for details.
