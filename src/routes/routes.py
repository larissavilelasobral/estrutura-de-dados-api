from flask import Blueprint
from src.controllers.books_controller import Controller

# coleção/namespace de rotas
books = Blueprint('books', __name__)
controller = Controller()


# marcador
@books.route('/', methods=['GET'])
def get_books():
    return controller.root()


@books.route('/books', methods=['GET'])
def get_books():
    return controller.get_books()


@books.route('/books', methods=['POST'])
def add_book():
    return controller.add_book()


@books.route('/books', methods=['POST'])
def delete_book():
    return controller.delete_book()
