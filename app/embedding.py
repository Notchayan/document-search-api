from sentence_transformers import SentenceTransformer
from typing import List, Dict
import numpy as np

class EmbeddingModel:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
    
    def embed_documents(self, documents: List[Dict[str, str]]) -> np.ndarray:
        """Generate embeddings for a list of documents"""
        texts = [doc["content"] for doc in documents]
        embeddings = self.model.encode(texts, show_progress_bar=True)
        return embeddings
    
    def embed_query(self, query: str) -> np.ndarray:
        """Generate embedding for a query string"""
        return self.model.encode([query])[0]