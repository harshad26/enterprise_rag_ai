from dotenv import load_dotenv
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

load_dotenv()

pdf_path = Path(__file__).parent / "profile.pdf"

# Load PDF files
loadFile = PyPDFLoader(file_path=pdf_path)
docs = loadFile.load()

# Spit doc into chunks
tetx_spitter = RecursiveCharacterTextSplitter(
  chunk_size = 1000,
  chunk_overlap = 400
)

chunks = tetx_spitter.split_documents(documents=docs)

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

print("This is done")