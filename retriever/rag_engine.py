import faiss
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

# Load from disk
def load_vector_store():
    with open("data/skills_db.json", "r") as f:
        docs = json.load(f)
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([d["text"] for d in docs])
    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(vectors.toarray())
    return docs, vectorizer, index

# RAG search
def search(query, vectorizer, index, docs, top_k=5):
    query_vec = vectorizer.transform([query]).toarray().astype('float32')
    _, I = index.search(query_vec, top_k)
    return [docs[i] for i in I[0]]
