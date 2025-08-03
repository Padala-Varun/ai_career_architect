import json
import faiss
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import os
import pickle

def build_index():
    print("Loading data...")
    with open("data/job_trends.json", "r") as f:
        data = json.load(f)

    print("Vectorizing text...")
    texts = [item["role"] + " " + item["skills"] + " " + item["trends"] for item in data]
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(texts).toarray().astype('float32')

    print("Building FAISS index...")
    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(vectors)

    print("Saving vectorizer and index...")
    os.makedirs("retriever", exist_ok=True)
    with open("retriever/vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)

    faiss.write_index(index, "retriever/faiss_index.idx")
    print("Done.")

build_index()
