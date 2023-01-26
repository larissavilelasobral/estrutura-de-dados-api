import uuid
from repository.books_repository import books_db  

class Book:
  
  def __init__(self, title, author):
      self.id = uuid.uuid4()
      self.título = title
      self.autor = author

  def get_book_by_id(id):
    for livro in books_db:
        if livro.id == id:
            return livro
    return None
  
  def atualizar_livro(id, título, autor):
    livro = Book.get_book_by_id(id)
    if livro:
        livro.título = título
        livro.autor = autor
        return True
    return False
  
  #buscar livros por autor