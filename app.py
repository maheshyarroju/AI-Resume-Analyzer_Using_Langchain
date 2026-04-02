import streamlit as st
import zipfile
import tempfile
import os
import pandas as pd



# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
/* Background */
.stApp {
    background: linear-gradient(135deg, #1f4037, #99f2c8);
    color: black;

}

/* SUCCESS MESSAGE FIX (WORKING) */       
div[data-testid="stAlert"] {
    background-color: #ffe6e6 !important;
    color: red !important;
    border-radius: 10px;
}
            

/* Title */
h1 {
    text-align: center;
    color: #ffffff;
    font-size: 40px;
}

/* Upload box */
.css-1cpxqw2, .stFileUploader {
    background-color: red;
    padding: 20px;
    border-radius: 10px;
}

/* Buttons */
.stDownloadButton button {
    background-color: white;
    color: red;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: bold;
}

.stDownloadButton button:hover {
    background-color: #0072ff;
}

/* Table */
.stDataFrame {
    background-color: white;
    border-radius: 10px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)




from dotenv import load_dotenv
from pypdf import PdfReader
from docx import Document

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

from pydantic import BaseModel, Field

# ---------------- LOAD API KEY ----------------

load_dotenv()  # reads GOOGLE_API_KEY from .env
os.environ["GOOGLE_API_KEY"] = os.getenv("gemini")

# ---------------- STREAMLIT UI ----------------
# st.title("📄 AI Resume Analyzer")

st.markdown("<h1>📄 AI Resume Analyzer</h1>", unsafe_allow_html=True)
st.markdown("### 🚀 Upload resumes & get structured insights instantly")

zip_file = st.file_uploader("Upload ZIP file containing resumes", type="zip")

# ---------------- READ FILES ----------------
def read_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

def read_docx(path):
    doc = Document(path)
    text = ""
    for para in doc.paragraphs:
        text += para.text
    return text

# ---------------- FIXED SCHEMA (STRUCTURED OUTPUT) ----------------
class ResumeSchema(BaseModel):
    name: str = Field(description="Candidate full name")
    email: str = Field(description="Email address")
    phone: str = Field(description="Phone number")
    skills: str = Field(description="Key skills")
    linkedin: str = Field(description="LinkedIn profile")
    summary: str = Field(description="Professional summary")

# ---------------- LLM ----------------
gemini = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0
)

# structured output parser
parser = gemini.with_structured_output(ResumeSchema)

# ---------------- PROMPT ----------------
prompt = PromptTemplate(
    template="""
Extract the following details from the resume text.

Resume Text:
{resume_text}
""",
    input_variables=["resume_text"],
)

# ---------------- MAIN LOGIC ----------------
if zip_file:

    results = []

    with tempfile.TemporaryDirectory() as temp_dir:

        zip_path = os.path.join(temp_dir, "resumes.zip")
        with open(zip_path, "wb") as f:
            f.write(zip_file.read())

        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(temp_dir)

        for file in os.listdir(temp_dir):

            file_path = os.path.join(temp_dir, file)

            if file.lower().endswith(".pdf"):
                resume_text = read_pdf(file_path)

            elif file.lower().endswith(".docx"):
                resume_text = read_docx(file_path)

            else:
                continue

            chain = prompt | parser
            output = chain.invoke({"resume_text": resume_text})

            results.append(output.dict())

    # ---------------- CSV OUTPUT ----------------
    df = pd.DataFrame(results)

    st.success("✅ Resumes analyzed successfully")
    st.dataframe(df)

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name="resume_data.csv",
        mime="text/csv"
    )