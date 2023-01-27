import uuid
from repository.books_repository import books_db  

class Book:
  def __init__(self, title, author):
      self.id = uuid.uuid4()
      self.title = title
      self.author = author

  def get_book_by_id(id):
    for book in books_db:
        if book.id == id:
            return book
    return None
  
  def update_book(id, title, author):
    book = Book.get_book_by_id(id)
    if book:
        book.title = title
        book.author = author
        return True
    return False
  
  #buscar livros por autor