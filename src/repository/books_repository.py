from flask import Flask, jsonify, request
from models.books import Book

class BooksRepository():
  def __init__(self):
    self.books_db = [
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
  
  def root(self):
    return "<h1>API em Flask<h1>"
 
  def get_books(self):
    return jsonify(self.books_db)
      
  def add_book(self, title, author):
    new_book = Book(title, author)
    self.books_db.append(new_book)
    # retornar o resultado em json? aqui no repository ou em controller
    return jsonify(new_book), 201
  
  def delete_book(self):
    if not len(self.books_db) == 0:
      del self.books_db[0]