from fastapi import FastAPI, Query, HTTPException
from typing import List

from app.data_loader import load_documents
from app.embedding import EmbeddingModel
from app.vector_store import VectorStore
from app.models import SearchResponse, SearchResult

app = FastAPI(title="Document Similarity Search API")

# Initialize components
embedding_model = EmbeddingModel()
documents = load_documents("data/sample_documents.txt")

if not documents:
    raise ValueError("No documents found! Please add documents to the data directory.")

# Generate embeddings
document_embeddings = embedding_model.embed_documents(documents)

# Initialize vector store
vector_store = VectorStore(dimension=document_embeddings.shape[1])
vector_store.add_documents(documents, document_embeddings)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Document Similarity Search API"}

@app.get("/api/search", response_model=SearchResponse)
def search_documents(q: str = Query(..., min_length=1, description="Search query")):
    if not q:
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    
    # Generate embedding for the query
    query_embedding = embedding_model.embed_query(q)
    
    # Search for similar documents
    search_results = vector_store.search(query_embedding, top_k=5)
    
    # Format results
    results = [
        SearchResult(
            id=doc["id"],
            content=doc["content"],
            similarity_score=score
        )
        for _, score, doc in search_results
    ]
    
    return SearchResponse(
        results=results,
        query=q,
        total_results=len(results)
    )

# Bonus: Add a new document endpoint
@app.post("/api/documents")
def add_document(content: str):
    global documents
    
    # Create new document
    new_id = str(len(documents))
    new_doc = {"id": new_id, "content": content}
    
    # Generate embedding
    new_embedding = embedding_model.embed_documents([new_doc])
    
    # Add to vector store
    vector_store.add_documents([new_doc], new_embedding)
    
    return {"id": new_id, "message": "Document added successfully"}