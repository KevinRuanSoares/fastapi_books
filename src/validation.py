from pydantic import BaseModel


class BookRequest(BaseModel):
    """BookRequest type"""

    book_id: int
    title: str
    author: str
    description: str
    rating: str
