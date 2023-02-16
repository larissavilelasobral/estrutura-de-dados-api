from flask import jsonify
from src.models.books import Book


class BooksRepository:
    def __init__(self):
        self.books_db = []

        self.books_db.append(Book('Código limpo: Habilidades práticas do Agile Software', 'Robert C. Martin'))
        self.books_db.append(Book('Arquitetura limpa: O guia para estrutura de software', 'Robert C. Martin'))
        self.books_db.append(Book('Microsserviços Prontos Para a Produção', 'Susan'))

    def root(self):
        return "<h1>API de Livros em Python/Flask!<h1>"

    def get_books(self):
        books = [book.__dict__ for book in self.books_db]
        response = {
            "data": books,
            "status_code": 200
        }
        return jsonify(response), 200
    # verificar nome se tem numero ou caractere especial
    # função de limpeza para tirar caracteres especiais

    def add_book(self, title, author):
        if not title or not author:
            return jsonify({"error": "Título e autor são obrigatórios."}), 400

        new_book = Book(title, author)
        self.books_db.append(new_book)

        response = {
            "data": [new_book.__dict__],
            "status_code": 201
        }

        return jsonify(response), 201

    def delete_book(self):
        if not self.books_db:
            return jsonify({"error": "Não há livros para serem deletados"}), 400

        book = self.books_db[0]
        del self.books_db[0]

        response = {
            "data": [book.__dict__],
            "message": "Livro deletado com sucesso",
            "status_code": 204
        }
        return jsonify(response), 204
        # padrão de response

    # {
    #     data: [
    #         {
    #             "author": "Robert C. Martin",
    #             "id": "3580aa47-6137-479c-9b88-5220d53238d1",
    #             "title": "Código limpo: Habilidades práticas do Agile Software"
    #         },
    #         {
    #             "author": "Robert C. Martin",
    #             "id": "69053f51-4580-4dab-851c-c688eab87e24",
    #             "title": "Arquitetura limpa: O guia para estrutura de software"
    #         }
    #     ],
    #  status_code: 201
    # }