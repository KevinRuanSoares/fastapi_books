class Book:
    """Book type"""

    book_id: int
    title: str
    author: str
    description: str
    rating: str

    def __init__(self, book_id: int, title: str, author: str, description: str, rating: str) -> None:
        self.book_id = book_id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
