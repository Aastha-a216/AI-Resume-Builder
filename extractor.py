
import re
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_info(text):
    info = {}
    doc = nlp(text)

    email = re.findall(r"\S+@\S+", text)
    info['email'] = email[0] if email else None

    phone = re.findall(r'\+?\d[\d\- ]{8,}\d', text)
    info['phone'] = phone[0] if phone else None

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            info['name'] = ent.text
            break

    skill_keywords = ["Python", "SQL", "Java", "Machine Learning", "Excel", "Pandas", "Numpy"]
    info['skills'] = [word for word in skill_keywords if word.lower() in text.lower()]

    return info
