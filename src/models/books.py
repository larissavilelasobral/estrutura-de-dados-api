import uuid

class Livro():
  def __init__(self, titulo, autor):
    # propriedades, inicializá-los com os valores passados como argumentos ao criar uma nova instância da classe
    # https://pt.wikipedia.org/wiki/Identificador_%C3%BAnico_universal
    self.id = uuid.uuid4() # utilizar uuid python generator
    self.titulo = titulo
    self.autor = autor
  
  # def alterar titulo()
  # def alterar autor()
  
  