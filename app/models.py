from pydantic import BaseModel
from typing import List, Optional

class Document(BaseModel):
    id: str
    content: str
    
class SearchResult(BaseModel):
    id: str
    content: str
    similarity_score: float
    
class SearchResponse(BaseModel):
    results: List[SearchResult]
    query: str
    total_results: int