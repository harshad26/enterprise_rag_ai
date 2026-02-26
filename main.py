from fastapi import FastAPI
from routes.delete_pdf import app as delete_router
from routes.process_pdf import app as process_router
from routes.search_data import app as search_router

app = FastAPI()

app.include_router(delete_router)
app.include_router(process_router)
app.include_router(search_router)
