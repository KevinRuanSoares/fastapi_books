from typing import List

from fastapi import APIRouter

from fakes.fake_book import books
from models import Book
from validation import BookRequest

router = APIRouter()


@router.get("/books")
async def read_all_books() -> List[Book]:
    return books


@router.post("/books/create_book")
async def create_book(body_request: BookRequest) -> None:
    new_book = Book(**body_request.dict())
    books.append(new_book)
