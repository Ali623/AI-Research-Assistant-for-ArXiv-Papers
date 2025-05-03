import json
from sentence_transformers import SentenceTransformer
import faiss
import os
import pickle

def chunk_text(text, chunk_size=500):
    sentences = text.split(". ")
    chunks, current = [], ""
    for sent in sentences:
        if len(current) + len(sent) < chunk_size:
            current += sent + ". "
        else:
            chunks.append(current.strip())
            current = sent + ". "
    if current:
        chunks.append(current.strip())
    return chunks

def build_faiss_index(papers_file="./data/papers.json", index_path="./data/faiss.index", meta_path="./data/meta.pkl"):
    model = SentenceTransformer("all-MiniLM-L6-v2")

    with open(papers_file) as f:
        papers = json.load(f)

    texts, metadata = [], []

    for paper in papers:
        chunks = chunk_text(paper["summary"])
        for chunk in chunks:
            texts.append(chunk)
            metadata.append({
                "title": paper["title"],
                "id": paper["id"]
            })

    embeddings = model.encode(texts, show_progress_bar=True)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    faiss.write_index(index, index_path)
    with open(meta_path, "wb") as f:
        pickle.dump(metadata, f)

    print(f"Saved FAISS index with {len(texts)} chunks.")

if __name__ == "__main__":
    build_faiss_index()
