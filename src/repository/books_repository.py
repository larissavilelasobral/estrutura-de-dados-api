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
        return jsonify(books)

    def add_book(self, title, author):
        if not title or not author:
            return jsonify({"error": "Título e autor são obrigatórios"}), 400

        new_book = Book(title, author)
        self.books_db.append(new_book)
        # método __dict__ permite tratar objetos de classe como dicionários, facilitando a manipulação de seus atributos.
        return jsonify(new_book.__dict__), 201

        # new_book = Book(title, author)
        # self.books_db.append(new_book)
        # json_string = json.dumps([obj.__dict__ for obj in self.books_db], ensure_ascii=False, indent=4)
        # return jsonify(json_string), 201

    def delete_book(self):
        if not self.books_db:
            return jsonify({"error": "Não há livros para serem deletados"}), 400

        book_title = self.books_db[0]
        del self.books_db[0]
        return jsonify({"message": "Livro deletado com sucesso", "book": book_title.__dict__}), 200
