from flask import jsonify, request
from repository.books_repository import BooksRepository

class Controller:
    def __init__(self):
        self.books_repository =  BooksRepository()
        
    def root(self):
        return self.books_repository.root()

    def get_books(self):
        
        return self.books_repository.get_books()

    def add_book(self,):
        body = request.get_json()
        
        title = body['name']
        author = body['author']
        
        return self.books_repository.add_book(title, author)

    def delete_book(self):
        return self.books_repository.delete_book()
    
