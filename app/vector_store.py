import faiss
import numpy as np
from typing import List, Dict, Tuple

class VectorStore:
    def __init__(self, dimension: int):
        self.dimension = dimension
        self.index = faiss.IndexFlatIP(dimension)  # Inner product by default
        self.documents = []
        
    def add_documents(self, documents: List[Dict[str, str]], embeddings: np.ndarray):
        """Add documents and their embeddings to the index"""
        if len(self.documents) == 0:
            self.documents = documents
        else:
            self.documents.extend(documents)
            
        # Normalize vectors for cosine similarity
        faiss.normalize_L2(embeddings)
        self.index.add(embeddings)
        
    def search(self, query_embedding: np.ndarray, top_k: int = 5) -> List[Tuple[int, float, Dict]]:
        """Search for most similar documents"""
        # Normalize query vector for cosine similarity
        query_embedding_normalized = query_embedding.reshape(1, -1)
        faiss.normalize_L2(query_embedding_normalized)
        
        # Search the index
        scores, indices = self.index.search(query_embedding_normalized, top_k)
        
        # Prepare results
        results = []
        for i, (score, idx) in enumerate(zip(scores[0], indices[0])):
            if idx < len(self.documents) and idx != -1:
                results.append((idx, float(score), self.documents[idx]))
                
        return results