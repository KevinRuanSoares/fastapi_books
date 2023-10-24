class Book:
    id: int
    title: str
    author: str
    description: str
    rating: str
    
    def __init__(self, id, title, author, decription, rating) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.decription = decription
        self.rating = rating