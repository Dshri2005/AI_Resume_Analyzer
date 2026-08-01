import pypdf as pdf
import docx as docx
import streamlit as st

def read_resume(resume):
    if resume is None:
        st.warning("Please upload a resume file.")
    else:
        ext = resume.name.split(".")[-1].lower()
        if ext == "pdf":
            reader = pdf.PdfReader(resume)
            text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
                    return text
        elif ext == "docx":
            reader = docx.Document(resume)
            text = ""
            for paragraph in reader.paragraphs:
                if paragraph.text.strip():
                    text+= paragraph.text + "\n"
            return text
        else:
            st.warning("Unsupposted file type. Please upload a PDF or a docx file.")
            return None

def clean_resume(resume: str) -> str:
    if resume is None:
        st.warning("Please upload a resume file.")
    else:
        # remove personal details, and other contact information from the resume text

def analyse_resume(processeed_resume, processed_job_desc):
    pass