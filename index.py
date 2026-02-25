from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

pdf_path = Path(__file__).parent / "profile.pdf"

# Load PDF files
loadFile = PyPDFLoader(file_path=pdf_path)
docs = loadFile.load()

# Spit doc into chunks
tetx_spitter = RecursiveCharacterTextSplitter(
  chunk_size = 1000,
  chunk_overlap = 400
)

tetx_spitter.split_documents(documents=docs)
