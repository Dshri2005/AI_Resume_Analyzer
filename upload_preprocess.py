import pypdf as pdf
import docx as docx
import streamlit as st
import re

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
        # 1. remove urls -- they break tokenizers
        resume = re.sub(r'http[s]?://\S+','', resume)
        resume = re.sub(r'www\.\S+', '', resume)

        #2. replace common bullet symbols with astandard space

        resume = re.sub(r'[\u2022\u2023\u25E6\u2043\u2219\uf0b7\uf0d8\uf0a7]',' ', resume)

        #3. remove any excessive tabs
        resume = re.sub(r'\t+',' ', resume)

        #4. remove speciall characters (excluding punctuations (,)./-, as they are needed for NLP)
        resume = re.sub(r'[^a-zA-Z0-9\s,\.\/\-]',' ', resume)

        return resume

def analyse_resume(processeed_resume, processed_job_desc):
    pass