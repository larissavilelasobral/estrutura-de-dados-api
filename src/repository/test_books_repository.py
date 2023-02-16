from flask import Flask
from src.repository.books_repository import BooksRepository

app = Flask(__name__)


# teste de integração
class TestBooksRepository:

    def setup(self):
        self.books_repository = BooksRepository()

    def test_add_book(self):
        with app.app_context():
            # arrange
            title = 'TDD com Python: Siga o Bode dos Testes'
            author = 'Harry J. W. Percival'

            # act
            result, status_code = self.books_repository.add_book(title, author)
            response_json = result.get_json()

            # condição, mensagem error
            # Assert
            assert status_code == 201
            assert response_json["title"] == title
            assert response_json["author"] == author

    def test_add_book_empaty_title(self):
        with app.app_context():
            # arrange
            test_title = ''
            test_author = 'Harry J. W. Percival'

            # act
            result, status_code = self.books_repository.add_book(test_title, test_author)
            response_json = result.get_json()

            # Assert
            assert status_code == 400
            assert response_json["error"] == "Título e autor são obrigatórios."
            assert response_json["title"] == test_title
            assert response_json["author"] == test_author

    def test_add_book_empaty_author(self):
        with app.app_context():
            # arrange
            test_title = 'TDD com Python: Siga o Bode dos Testes'
            test_author = ''

            # act
            result, status_code = self.books_repository.add_book(test_title, test_author)
            response_json = result.get_json()

            # Assert
            assert status_code == 400
            assert response_json["error"] == "Título e autor são obrigatórios."
            assert response_json["title"] == test_title
            assert response_json["author"] == test_author

    def test_delete_book(self):
        with app.app_context():
            # arrange
            book = self.books_repository.books_db[0]
            expected_title = book.title

            # act
            result, status_code = self.books_repository.delete_book()
            response_json = result.get_json()

            # assert
            assert status_code == 200
            assert response_json['message'] == 'Livro deletado com sucesso'
            assert response_json['book']['title'] == expected_title
