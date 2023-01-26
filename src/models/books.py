import uuid
from repository.books_repository import livros  

class Livro:
  
  def __init__(self, título, autor):
    # atributos do livro
    # o construtor inicializa esses atributos quando um objeto da classe Livro é criado
      self.id = uuid.uuid4()
      self.título = título
      self.autor = autor

# metodos para obter e atualizar informações sobre um livro especifico ou para adicionar e remover livros da lista
  def obter_livro(id):
    for livro in livros:
        if livro.id == id:
            return livro
    return None
  
  def atualizar_livro(id, título, autor):
    # retorna livro
    livro = Livro.obter_livro(id)
    if livro:
        livro.título = título
        livro.autor = autor
        return True
    return False
  
  #buscar livros por autor