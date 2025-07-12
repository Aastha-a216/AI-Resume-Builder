
from pdfminer.high_level import extract_text
from docx import Document

def extract_text_from_pdf(file_path):
    return extract_text(file_path)

def extract_text_from_docx(file_path):
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def get_text(uploaded_file):
    import tempfile
    suffix = ".pdf" if uploaded_file.name.endswith(".pdf") else ".docx"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    if suffix == ".pdf":
        return extract_text_from_pdf(tmp_path)
    else:
        return extract_text_from_docx(tmp_path)
