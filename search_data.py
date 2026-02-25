from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI
load_dotenv()

openAI_client = OpenAI()

#Vector Embedding
embedding_model = OpenAIEmbeddings(
  model="text-embedding-3-large"
)

vector_db=QdrantVectorStore.from_existing_collection(
  url="http://localhost:6333",
  collection_name="enterprise_rag",
  embedding=embedding_model
)

# Search input
search_query = input("Search: ")

# Find relevant chunks from vector DB
search_results = vector_db.similarity_search(query=search_query)

context = "\n\n\n".join([search.page_content for search in search_results])

SYSTEM_PROMPT = f"""
You are a helpful AI Assistant who answers of the search query based on the available context.

Context:
{context}
"""

response = openAI_client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": search_query}
  ]
)

print(f"Final search: ", response.choices[0].message.content)

