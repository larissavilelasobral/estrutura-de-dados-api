from flask import Blueprint
from src.controllers.books_controller import Controller

controller = Controller()

books = Blueprint('books', __name__)


@books.route('/', methods=['GET'])
def root():
    return controller.root()


@books.route('/books', methods=['GET'])
def get_books():
    return controller.get_books()


@books.route('/book', methods=['POST'])
def add_book():
    return controller.add_book()


@books.route('/book', methods=['DELETE'])
def delete_book():
    return controller.delete_book()
