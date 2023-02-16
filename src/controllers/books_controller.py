from flask import request
from src.repository.books_repository import BooksRepository


class Controller:
    def __init__(self):
        self.books_repository = BooksRepository()

    def root(self):
        return self.books_repository.root()

    def get_books(self):
        return self.books_repository.get_books()

    def add_book(self, ):
        body = request.get_json()

        title = body['title']
        author = body['author']
        # pegar mais dados para fazer mais regras de negocio, tratar os dados e realizar testes

        return self.books_repository.add_book(title, author)

    def delete_book(self):
        return self.books_repository.delete_book()
