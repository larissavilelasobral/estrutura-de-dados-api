from flask import Flask, jsonify, request

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

# https://medium.com/@pererikbergman/repository-design-pattern-e28c0f3e4a30
class BooksRepository():
  def __init__(self):
    print('BooksReposiroey')
  # def get books
  # def adicionar
  # deletar
  
  def add_book(self):
    body = request.get_json()
    
    #ternária
    new_id = len(livros) + 1 if livros else 1
    
    novo_livro = {
      "id": new_id,
      "título": body["título"],
      "autor": body["autor"]
    }

    livros.append(novo_livro)
    
    return novo_livro, 201
  
  def delete_book(self):
    # primeiro elemento a ser adicionado é o primeiro a ser removido.
      if not len(livros) == 0:
        del livros[0]
        
      return livros
