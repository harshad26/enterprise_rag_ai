from dotenv import load_dotenv
from fastapi import APIRouter
from services.search_services import seach_by_query
from schemas.search_schema import SearchRequest

load_dotenv()

app = APIRouter()

@app.post("/search")
def search(data: SearchRequest):
  response = seach_by_query(data.query)

  return {"results": response.choices[0].message.content}
