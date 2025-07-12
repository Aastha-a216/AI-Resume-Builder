🚀 AI-Powered Resume Parser & Job Matcher
An advanced Python application that parses resumes (PDF/DOCX), extracts key information using NLP, and matches candidate profiles with job descriptions using semantic similarity powered by BERT embeddings.

💡 Features
✅ Parse resumes in PDF or DOCX formats

✅ Extract key details: Name, Email, Phone, Skills

✅ Match resume content to job descriptions using BERT-based similarity

✅ Interactive UI built with Streamlit

✅ Real-time matching score visualization

🧰 Tech Stack
Python

spaCy for NLP-based entity extraction

pdfminer.six & python-docx for parsing documents

sentence-transformers for BERT-based embeddings

Streamlit for frontend

⚙️ Installation

git clone https://github.com/yourusername/resume-matcher.git
cd resume-matcher
pip install -r requirements.txt
python -m spacy download en_core_web_sm

🚀 Usage

streamlit run app.py

Upload a resume file (PDF or DOCX).

Paste your job description.

View extracted resume details and a match score.

🗂️ Project Structure

resume_matcher/
├── app.py            # Streamlit application
├── parser.py         # Resume file parsing logic
├── extractor.py      # NLP-based info extractor
├── matcher.py        # Similarity computation using BERT
├── requirements.txt
