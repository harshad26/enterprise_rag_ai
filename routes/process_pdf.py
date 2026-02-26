from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from fastapi import APIRouter, UploadFile, File, Form
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_community.document_loaders import PyPDFLoader
import shutil
import os

load_dotenv()

app = APIRouter()

@app.post("/process-pdf")
async def process_pdf(document_id: int = Form(...), file: UploadFile = File(...)):
  os.makedirs("temp", exist_ok=True)
  file_location = f"temp/{file.filename}"

  with open(file_location, "wb") as buffer:
    shutil.copyfileobj(file.file, buffer)

  chunks = chunk_pdf(file_location, document_id)
  return {"message": "PDF processed successfully", "chunks": len(chunks)}

# take a PDF file and chunk it then store it into Vectore DB...
def chunk_pdf(file_location, document_id):
  loader = PyPDFLoader(file_location)
  docs = loader.load()

  text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400
  )

  chunks = text_splitter.split_documents(docs)

  # added metadata which useful later to remove
  for i, chunk in enumerate(chunks):
    chunk.metadata["document_id"] = document_id
    chunk.metadata["chunk_index"] = i
    chunk.metadata["source"] = "pdf"
    
  # Vector Embedding
  embedding_model = OpenAIEmbeddings(
    model = "text-embedding-3-large"
  )

  vectore_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="enterprise_rag"
  )
  return chunks
