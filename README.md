# Document Search API

A semantic document search API that finds similar documents using vector embeddings and efficient similarity search techniques.

## Overview

This API provides semantic search capabilities for text documents. It:
- Converts documents into vector embeddings using sentence transformers
- Stores these embeddings in a FAISS vector database
- Exposes endpoints to search for documents similar to a given query
- Supports adding new documents in real-time

## Features

- Semantic search using vector embeddings
- Fast and efficient similarity matching with FAISS
- Real-time indexing for new documents
- RESTful API with FastAPI
- Containerized deployment with Docker

## Requirements

- Docker and Docker Compose installed on your system
- Internet connection (for initial container build and model download)

## Installation & Setup

### Prerequisites

Make sure you have Docker and Docker Compose installed:

- **Mac**: [Docker Desktop for Mac](https://docs.docker.com/desktop/install/mac-install/)
- **Windows**: [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/)
- **Ubuntu**:
  ```bash
  sudo apt-get update
  sudo apt-get install docker.io docker-compose
  sudo systemctl start docker
  sudo systemctl enable docker
  ```

### Getting Started

1. **Clone the repository** (or download and extract the ZIP)

2. **Navigate to the project directory**:
   ```bash
   cd document-search-api
   ```

3. **Build and start the Docker container**:
   ```bash
   docker-compose up -d
   ```
   
   The first time you run this command, Docker will:
   - Build the container image
   - Download the required dependencies
   - Download the sentence transformer model
   - Start the API service

4. **Verify the API is running**:
   Open your browser and navigate to: http://localhost:8000/
   
   You should see a welcome message.

## Usage

Once the API is running, you can:

### Search for documents

Visit in your browser:
```
http://localhost:8000/api/search?q=your search query here
```

Or use curl:
```bash
curl "http://localhost:8000/api/search?q=machine%20learning"
```

### Add a new document

Using curl:
```bash
curl -X POST "http://localhost:8000/api/documents" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "content=Your new document text here"
```

## API Endpoints

- `GET /`: Welcome message
- `GET /api/search?q=<query>`: Search for documents similar to the query
- `POST /api/documents`: Add a new document to the vector database

## Managing the Docker Container

### Stop the container:
```bash
docker-compose down
```

### View logs:
```bash
docker-compose logs -f
```

### Restart the container:
```bash
docker-compose restart
```

## Sample Data

The system comes pre-loaded with 10 sample documents about programming, APIs, and machine learning concepts.

## Data Persistence

Any documents you add will be stored in the container. If you want to persist your data, we're using a volume mount in docker-compose.yml that links to the `./data` directory in your project folder.

## Troubleshooting

- **API not accessible**: Make sure port 8000 is not in use by another application
- **Slow first query**: The first search might be slightly slower as the model loads into memory
