
import streamlit as st
from parser import get_text
from extractor import extract_info
from matcher import compute_similarity

st.title("AI Resume Parser & Job Matcher")

uploaded_resume = st.file_uploader("Upload Resume (.pdf/.docx)")
job_desc = st.text_area("Paste Job Description")

if uploaded_resume and job_desc:
    resume_text = get_text(uploaded_resume)
    info = extract_info(resume_text)
    similarity = compute_similarity(resume_text, job_desc)

    st.subheader("Extracted Information")
    st.json(info)

    st.subheader("Match Score")
    st.success(f"Similarity with Job Description: {similarity * 100:.2f}%")
