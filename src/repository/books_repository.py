from flask import jsonify
from src.models.books import Book


class BooksRepository:

    def __init__(self):
        self.books_db = [
            {
                'id': 1,
                'title': 'Código limpo: Habilidades práticas do Agile Software',
                'author': 'Robert C. Martin'
            },
            {
                'id': 2,
                'title': 'Arquitetura limpa: O guia para estrutura de software',
                'author': 'Robert C. Martin'
            },
            {
                'id': 3,
                'title': 'Microsserviços Prontos Para a Produção',
                'author': 'Susan J. Fowler'
            },
            {
                'id': 4,
                'title': 'Domain-Driven Design: Atacando as complexidades do software',
                'author': 'Eric Evans'
            },
            {
                'id': 5,
                'title': 'Refatoração: Aperfeiçoando o Design de Códigos',
                'author': 'Martin Fowler'
            },
            {
                'id': 6,
                'title': 'O Programador Pragmático: De Aprendiz a Mestre',
                'author': 'Andrew Hunt & David Thomas'
            },
            {
                'id': 7,
                'title': 'Entendendo Algoritmos: Um Guia Ilustrado Para Programadores',
                'author': 'Aditya Y. Bhargava'
            },
            {
                'id': 8,
                'title': 'Estruturas de Dados e Algoritmos com JavaScript',
                'author': 'Loiane Groner'
            },
            {
                'id': 9,
                'title': 'Aprendendo TypeScript: Melhore Suas Habilidades',
                'author': 'Josh Goldberg'
            },
            {
                'id': 10,
                'title': 'Linux Eficiente na Linha de Comando',
                'author': 'Daniel J. Barrett'
            },
        ]

    def root(self):
        return "<h1>API em Flask<h1>"

    def get_books(self):
        return jsonify(self.books_db)

    def add_book(self, title, author):
        if not title or not author:
            return jsonify({"error": "Título e autor são obrigatórios"}), 400

        new_book = Book(title, author)

        obj = {
            'id': new_book.id,
            'title': new_book.title,
            'author': new_book.author
        }

        self.books_db.append(obj)

        return jsonify(new_book), 201

    def delete_book(self):
        if not self.books_db:
            return jsonify({"error": "Não há livros para serem deletados"}), 400

        del self.books_db[0]
        return jsonify({"message": "Livro deletado com sucesso"}), 200
