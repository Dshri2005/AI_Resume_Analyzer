import streamlit as st
import upload_preprocess as up

st.set_page_config(page_title="Resume Analyzer and Job Recommender", page_icon=":briefcase:", layout="wide")
st.title("AI Resume Analyzer and Job Recommender")

try:
    resume =st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])
    job_desc = st.text_area("Paste your job description below")
except Exception as e:
    st.error(f"An error occurred: {e}")

processed_resume =up.preprocess_resume(resume)
processed_job_desc = up.preprocess_job_desc(job_desc)

read_resume = up.read_resume(resume)
clean_resume = up.clean_resume(read_resume)
up.analyse_resume(processed_resume, processed_job_desc)