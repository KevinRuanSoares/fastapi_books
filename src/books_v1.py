from typing import List

from fastapi import APIRouter, Body

from validation import BookRequest

router = APIRouter()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "science"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
    {"title": "Title Four", "author": "Author Four", "category": "math"},
    {"title": "Title Five", "author": "Author Five", "category": "math"},
    {"title": "Title Six", "author": "Author Two", "category": "math"},
]


@router.get("/books")
async def read_all_books() -> List[dict]:
    return BOOKS


@router.get("/books/{book_title}")
async def read_book(book_title: str) -> dict:
    for book in BOOKS:
        if book.get("title", "").casefold() == book_title.casefold():
            return book
    return {}


@router.get("/books/")
async def read_category_by_query(category: str) -> List[dict]:
    books_to_return = []
    for book in BOOKS:
        if book.get("category", "").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@router.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str) -> List[dict]:
    books_to_return = []
    for book in BOOKS:
        if (
            book.get("author", "").casefold() == book_author.casefold()
            and book.get("category", "").casefold() == category.casefold()
        ):
            books_to_return.append(book)
    return books_to_return


@router.post("/books/create_book")
async def create_book(new_book: BookRequest = Body()) -> None:
    BOOKS.append(new_book)
