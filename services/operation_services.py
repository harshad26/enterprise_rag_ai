from qdrant_client import QdrantClient
from qdrant_client.models import Filter, FieldCondition, MatchValue

client = QdrantClient(url="http://localhost:6333")

# Function to find docuemnt id from collection and delete
def delete_by_document_id(document_id: int):
  client.delete(
      collection_name="enterprise_rag",
      points_selector=Filter(
          must=[
              FieldCondition(
                  key="metadata.document_id",
                  match=MatchValue(value=document_id)
              )
          ]
      )
  )
