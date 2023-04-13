from flask import request

from src.controllers.responses.error.error import ApiException, ErrorResponse
from src.controllers.responses.success.success import SuccessResponse
from src.repository.books_repository import BooksRepository
from src.service.service import BooksService


class Controller:
    def __init__(self):
        self.books_repository = BooksRepository()
        self.books_service = BooksService()

    def root(self):
        return self.books_repository.root()

    def get_books(self):
        return self.books_repository.get_books()

    def add_book(self):
        try:
            body = request.get_json()
            return self.books_service.handle_book(body)
        except ApiException as e:
            return ErrorResponse(str(e), e.status_code).to_dict()
        except Exception as e:
            return ErrorResponse('Internal server error', 500).to_dict()

    def delete_book(self):
        try:
            book_id = request.args.get('id')

            if not book_id:
                raise ApiException('Missing book ID', 400)

            deleted = self.books_repository.delete_book(book_id)

            if not deleted:
                raise ApiException('Book not found', 404)

            return SuccessResponse('Book deleted successfully', 200).to_dict()
        except ApiException as e:
            return ErrorResponse(str(e), e.status_code).to_dict()
        except Exception as e:
            return ErrorResponse('Internal server error', 500).to_dict()
