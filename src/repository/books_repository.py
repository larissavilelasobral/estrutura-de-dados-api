from flask import jsonify
from src.models.books import Book


class BooksRepository:
    def __init__(self):
        self.books_db = []

        self.books_db.append(Book(
            'Código limpo: Habilidades práticas do Agile Software',
            'Robert C. Martin',
            'Este livro é uma referência essencial para qualquer programador que queira escrever código mais legível, '
            'sustentável e de alta qualidade.',
            'Alta Books',
            '2010',
            '464',
            '978-8576082675',
            'Português',
            'Tecnologia/Programação',
            'Sem Imagem'
        ))
        self.books_db.append(Book(
            'Arquitetura limpa: O guia para estrutura de software',
            'Robert C. Martin',
            'Neste livro, o autor apresenta um guia prático para a criação de arquiteturas de software limpas e '
            'sustentáveis.',
            'Novatec Editora',
            '2018',
            '432',
            '978-8575227249',
            'Português',
            'Tecnologia/Programação',
            'Sem Imagem'
        ))

    def root(self):
        return "<h1>API de Livros em Python/Flask!<h1>"

    def get_books(self):
        books = [book.__dict__ for book in self.books_db]
        response = {
            "data": books,
            "status_code": 200
        }
        return jsonify(response), 200

    def add_book(self, title, author, description, publisher, publication_date, num_pages, isbn, language, genre, cover_image):
        if not title or not author:
            return jsonify({"error": "Título e autor são obrigatórios."}), 400

        new_book = Book(title, author, description, publisher, publication_date, num_pages, isbn, language, genre, cover_image)
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
        # não retorna nenhuma mensagem na api?
        response = {
            "data": [book.__dict__],
            "message": "Livro deletado com sucesso",
            "status_code": 204
        }
        return jsonify(response), 204
