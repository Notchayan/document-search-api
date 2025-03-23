import os
from typing import List, Dict

def load_documents(data_path: str) -> List[Dict[str, str]]:
    """
    Load documents from a directory or file
    Returns a list of dictionaries with 'id' and 'content' keys
    """
    documents = []
    
    # Simple text file loader (one document per line)
    if os.path.isfile(data_path) and data_path.endswith('.txt'):
        with open(data_path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                if line.strip():  # Skip empty lines
                    documents.append({
                        'id': str(i),
                        'content': line.strip()
                    })
    
    # Add more data loading methods as needed (e.g., CSV, JSON, etc.)
    
    return documents