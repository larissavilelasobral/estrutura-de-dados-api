import uuid
from src.repository.books_repository import BooksRepository

# organização/estruturar banco 
class Book:
    books_db = BooksRepository()
    def __init__(self, title, author):
        self.id = uuid.uuid4()
        self.title = title
        self.author = author

    def get_book_by_id(self, book_id):
        for book in books_db.:
            if book.id == book_id:
                return book
        return None

    def update_book(self, book_id, title, author):
        book = Book.get_book_by_id(book_id)
        if book:
            book.title = title
            book.author = author
            return True
        return False
