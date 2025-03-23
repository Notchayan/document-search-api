FROM python:3.10-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --timeout 300

# Copy application code
COPY . .

# Create data directory if it doesn't exist
RUN mkdir -p data

# Add sample data if not already present
RUN if [ ! -f data/sample_documents.txt ]; then \
    echo "Python is a versatile programming language with clean syntax and extensive libraries." > data/sample_documents.txt && \
    echo "FastAPI is a modern, fast web framework for building APIs with Python based on standard type hints." >> data/sample_documents.txt && \
    echo "Vector embeddings are numerical representations of text that capture semantic meaning." >> data/sample_documents.txt && \
    echo "FAISS is a library for efficient similarity search developed by Facebook Research." >> data/sample_documents.txt && \
    echo "Sentence transformers convert text into fixed-size embeddings that capture meaning." >> data/sample_documents.txt && \
    echo "Machine learning algorithms learn patterns from data without being explicitly programmed." >> data/sample_documents.txt && \
    echo "Natural Language Processing (NLP) enables computers to understand and process human language." >> data/sample_documents.txt && \
    echo "APIs provide a structured way for different software applications to communicate with each other." >> data/sample_documents.txt && \
    echo "Semantic search goes beyond keyword matching to understand the intent behind a query." >> data/sample_documents.txt && \
    echo "Cosine similarity measures the cosine of the angle between two non-zero vectors in a vector space." >> data/sample_documents.txt; \
    fi

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]