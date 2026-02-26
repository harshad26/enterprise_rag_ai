# Enterprise RAG AI

A robust, enterprise-grade Retrieval-Augmented Generation (RAG) backend API built with FastAPI, LangChain, Qdrant Vector Database, and OpenAI.

This project allows you to ingest PDF documents into a local Qdrant vector database using OpenAI's state-of-the-art embedding models (`text-embedding-3-large`) and perform contextualized RAG searches against them using `gpt-4o`.

## Features
- **PDF Ingestion & Processing:** Upload and chunk PDF documents into searchable vector embeddings.
- **Semantic Search & RAG:** Query the uploaded context, retrieve relevant text, and generate accurate AI-assisted responses.
- **Document Management:** Remove or manage previously uploaded PDFs.
- **Local Vector Database:** Quick and scalable semantic lookups powered by Qdrant.

## Technology Stack
- **Web Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **Large Language Models:** [OpenAI](https://openai.com/) (GPT-4o) and Embeddings (text-embedding-3-large)
- **RAG & Orchestration:** [LangChain](https://www.langchain.com/)
- **Vector Database:** [Qdrant](https://qdrant.tech/)

## Prerequisites
- **Python 3.10+** (or compatible)
- **Docker** (recommended for running Qdrant locally)
- **OpenAI API Key**

## Setup & Installation

**1. Clone the repository**
```bash
git clone <your-repository-url>
cd enterprise_rag_ai
```

**2. Virtual Environment Setup (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

**3. Install Dependencies**
```bash
pip install -r requirement.txt
```

**4. Start Local Qdrant Server**
If you have Docker available, you can quickly spin up Qdrant locally:
```bash
docker run -p 6333:6333 qdrant/qdrant
```
*(Optionally use the provided `docker-compose.yml` if configured)*

**5. Environment Variables**
Ensure you have a `.env` file at the root of your project directory containing:
```
OPENAI_API_KEY=your_actual_openai_api_key_here
```

## Running the Application

To start the FastAPI server, use Uvicorn:

```bash
uvicorn main:app --reload
```

The application will be running on `http://127.0.0.1:8000`.
You can access the automated Swagger UI documentation at `http://127.0.0.1:8000/docs`.

## API Endpoints Overview

The application is structured into specific route modules:
- `/process` - PDF processing endpoints (`routes/process_pdf.py`)
- `/delete`  - PDF deletion endpoints (`routes/delete_pdf.py`)
- `/search`  - Natural language querying and completion endpoints (`routes/search_data.py`)

*See the Swagger UI (`/docs`) for the full API specification and easy testing forms.*

## Project Structure

```text
enterprise_rag_ai/
├── main.py                 # Main FastAPI application entrypoint
├── requirement.txt         # Project dependencies
├── docker-compose.yml      # Docker compose configuration (e.g., Qdrant)
├── .env                    # Environment variables file (not tracked by Git)
├── routes/                 # FastAPI router definitions
│   ├── process_pdf.py      # PDF ingestion routes
│   ├── delete_pdf.py       # PDF deletion routes
│   └── search_data.py      # Search routes
├── services/               # Core business logic processing
│   └── search_services.py  # LangChain/OpenAI interaction scripts
├── schemas/                # Pydantic validation models
└── temp/                   # Temporary file storage (e.g., PDF uploads)
```

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
MIT License.
