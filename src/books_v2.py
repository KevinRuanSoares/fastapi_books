from fastapi import Body, APIRouter
from interfaces import Book

router = APIRouter()

BOOKS = [
    Book(1, "The Mysterious Island", "Jules Verne", "A novel about the adventures of a group of castaways on a deserted island.", "4.5"),
    Book(2, "1984", "George Orwell", "A dystopian novel set in a totalitarian future.", "4.4"),
    Book(3, "To Kill a Mockingbird", "Harper Lee", "A novel dealing with issues of racism and morality.", "4.8"),
    Book(4, "Pride and Prejudice", "Jane Austen", "A romantic novel dealing with manners and upbringing.", "4.2"),
    Book(5, "The Great Gatsby", "F. Scott Fitzgerald", "A novel about American society during the Roaring Twenties.", "4.1"),
    Book(6, "Moby-Dick", "Herman Melville", "A novel about the voyage of the whaling ship Pequod.", "3.9"),
    Book(7, "War and Peace", "Leo Tolstoy", "An epic novel about French invasion of Russia.", "4.3"),
    Book(8, "The Catcher in the Rye", "J.D. Salinger", "A novel about the experiences of a 16-year-old boy in New York City.", "4.0"),
    Book(9, "Brave New World", "Aldous Huxley", "A dystopian novel about a technologically advanced future society.", "4.1"),
    Book(10, "Ulysses", "James Joyce", "A novel that parallels a day in the life of Leopold Bloom with Homer's Odyssey.", "3.8")
]

@router.get("/books") 
async def read_all_books():
  return BOOKS
