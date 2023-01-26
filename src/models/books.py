import uuid
  
class Livro:
  
  livros = [
  {
      'id': 1,
      'título': 'Código limpo: Habilidades práticas do Agile Software',
      'autor': 'Robert C. Martin'
  },
  {
      'id': 2,
      'título': 'Arquitetura limpa: O guia para estrutura de software',
      'autor': 'Robert C. Martin'
  },
  {
      'id': 3,
      'título': 'Microsserviços Prontos Para a Produção',
      'autor': 'Susan J. Fowler'
  },
  {
      'id': 4,
      'título': 'Domain-Driven Design: Atacando as complexidades do software',
      'autor': 'Eric Evans'
  },
  {
      'id': 5,
      'título': 'Refatoração: Aperfeiçoando o Design de Códigos',
      'autor': 'Martin Fowler'
  },
  {
      'id': 6,
      'título': 'O Programador Pragmático: De Aprendiz a Mestre',
      'autor': 'Andrew Hunt & David Thomas'
  },
  {
      'id': 7,
      'título': 'Entendendo Algoritmos: Um Guia Ilustrado Para Programadores',
      'autor': 'Aditya Y. Bhargava'
  },
  {
      'id': 8,
      'título': 'Estruturas de Dados e Algoritmos com JavaScript',
      'autor': 'Loiane Groner'
  },
  {
      'id': 9,
      'título': 'Aprendendo TypeScript: Melhore Suas Habilidades',
      'autor': 'Josh Goldberg'
  },
  {
      'id': 10,
      'título': 'Linux Eficiente na Linha de Comando',
      'autor': 'Daniel J. Barrett'
  },
]
  
  def __init__(self, título, autor):
    # atributos do livro
    # o construtor inicializa esses atributos quando um objeto da classe Livro é criado
      self.id = uuid.uuid4()
      self.título = título
      self.autor = autor

# metodos para obter e atualizar informações sobre um livro especifico ou para adicionar e remover livros da lista
  def obter_livro(id):
    for livro in Livro.livros:
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