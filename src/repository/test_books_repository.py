import unittest
from src.repository.books_repository import BooksRepository

from flask import Flask

app = Flask(__name__)


class TestBooksRepository(unittest.TestCase):

    def setUp(self):
        self.books_repository = BooksRepository()

    def test_delete_book(self):
        with app.app_context():
            # arrange
            book = self.books_repository.books_db[0]
            expected_title = book.title

            # act
            result, status_code = self.books_repository.delete_book()
            response_json = result.get_json()

            # assert
            self.assertEqual(status_code, 200)
            self.assertEqual(response_json['message'], 'Livro deletado com sucesso')
            self.assertEqual(response_json['book']['title'], expected_title)


if __name__ == '__main__':
    unittest.main()
