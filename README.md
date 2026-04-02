# 🧠 AI-Powered Resume Analyzer & CSV Generator

Built with LangChain, Google Gemini & Streamlit

🎥 Demo Video: https://drive.google.com/file/d/1nkm5GVJUvKZMqQ7fM8EmZ51CQWVInKBe/view?usp=sharing

## 📌 Project Overview

In real-world hiring scenarios, recruiters often receive a large number of resumes, usually bundled in ZIP files containing PDFs and Word documents. Reviewing each resume manually takes a lot of time and effort, and the extracted information is not always consistent.

To solve this problem, I developed an AI-based system that can automatically read and analyze resumes, and convert them into structured data using Large Language Models.

## 🎯 Problem Statement

Handling resumes at scale comes with several challenges:

- Processing hundreds of resumes manually is time-consuming
- Resume formats vary (PDF, DOCX, different layouts)
- Extracting key details like skills and contact info is inconsistent
- No structured format makes filtering and analysis difficult

## 💡 Solution Approach

To address these issues, I built an intelligent pipeline using LangChain and Google Gemini that:

- Accepts resumes in bulk through a ZIP file
- Extracts text from both PDF and DOCX formats
- Uses an LLM to understand and structure the content
- Ensures consistent output using a predefined schema
- Converts all extracted data into a CSV file for easy usage

## 🚀 Key Features

- Upload a ZIP file containing multiple resumes
- Automatically processes PDF and Word documents
- Extracts important candidate details using AI
- Converts unstructured data into structured format
- Generates a downloadable CSV file via Streamlit UI

## 🛠️ Tech Stack

- Python – Core programming
- Streamlit – User interface
- LangChain – LLM workflow management
- Google Gemini – Resume understanding
- Pydantic / TypedDict – Structured output
- pypdf – PDF parsing
- python-docx – DOCX parsing
- Pandas – Data processing and CSV generation

## 📂 Project Structure

```AI-Resume-Analyzer/
│
├── app.py              # Streamlit app
├── requirements.txt   # Dependencies
├── .env               # API keys 
├── README.md         # Documentation ```


## 🔑 Environment Setup

Create a .env file and add your API key:

GOOGLE_API_KEY = your_api_key_here

## 📦 Installation

pip install -r requirements.txt

## ▶️ Run the Application

streamlit run app.py

## 📊 Output (Structured Data)

Each resume is converted into structured fields such as:

Name
Email
Phone Number
Skills
LinkedIn Profile
Professional Summary

All extracted records are saved into a CSV file for easy download and analysis.

## 📈 Use Cases

Resume screening for HR teams
Pre-processing for Applicant Tracking Systems (ATS)
Candidate filtering based on skills
Talent data analysis

## 🔮 Future Improvements

Matching resumes with job descriptions
Candidate ranking and scoring system
Dashboard for skill analytics
Integration with databases (PostgreSQL / MongoDB)
Support for multilingual resumes

## 🏁 Conclusion

This project shows how LLMs and LangChain can simplify real-world recruitment workflows. By converting unstructured resumes into structured data automatically, it saves time, reduces manual effort, and improves consistency in hiring processes.