
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_similarity(resume_text, job_desc):
    embeddings = model.encode([resume_text, job_desc])
    similarity = util.cos_sim(embeddings[0], embeddings[1])
    return round(float(similarity), 2)
