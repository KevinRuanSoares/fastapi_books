from fastapi import FastAPI

from books_v1 import router as books_router_v1
from books_v2 import router as books_router_v2

app = FastAPI()


app.include_router(books_router_v1, prefix="/v1")
app.include_router(books_router_v2, prefix="/v2")
