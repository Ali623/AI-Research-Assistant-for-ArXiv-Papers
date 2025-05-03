import faiss
import pickle
from sentence_transformers import SentenceTransformer

class RAGRetriever:
    def __init__(self, index_path="../data/faiss.index", meta_path="../data/meta.pkl"):
        self.index = faiss.read_index(index_path)
        with open(meta_path, "rb") as f:
            self.metadata = pickle.load(f)
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def search(self, query, top_k=5):
        query_embedding = self.model.encode([query])
        D, I = self.index.search(query_embedding, top_k)

        results = []
        for i in I[0]:
            if i < len(self.metadata):
                results.append(self.metadata[i] | {"chunk": self.metadata[i].get("chunk", "")})
        return results
