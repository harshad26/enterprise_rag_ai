from dotenv import load_dotenv
from fastapi import APIRouter
from services.operation_services import delete_by_document_id
from schemas.delete_schema import DeleteRequest

load_dotenv()

app = APIRouter()

@app.post("/delete-pdf")
def delete_document(data: DeleteRequest):
  delete_by_document_id(data.document_id)
  return {"status": "deleted", "document_id": data.document_id}
