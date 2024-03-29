import json
import unittest
from flask import Flask

from src.repository.books_repository import BooksRepository

app = Flask(__name__)


# teste de integração
class TestBooksRepository(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.books_repository = BooksRepository()

    def test_get_books(self):
        # criar contexto flesk para acessar
        with self.app.app_context():
            response, status_code = self.books_repository.get_books()
            self.assertEqual(status_code, 200)
            response_data = json.loads(response.data)
            self.assertEqual(len(response_data['data']), 2)

    def test_add_book(self):
        # arrange
        title = 'TDD com Python: Siga o Bode dos Testes'
        author = 'Harry J. W. Percival'
        description = 'Este livro é uma referência essencial para qualquer programador que queira escrever código mais legível.'
        publisher = 'Alta Books'
        publication_date = '2010'
        num_pages = '464'
        isbn = '978-8576082675'
        language = 'Português'
        genre = 'Tecnologia/Programação'
        cover_image = 'Sem Imagem'

        # act
        response, status_code = self.books_repository.add_book(title, author, description, publisher, publication_date, num_pages, isbn, language, genre, cover_image)
        new_book = json.loads(response.data)['data'][0]

        # Assert
        self.assertEqual(status_code, 201)
        self.assertEqual(new_book['title'], title)
        self.assertEqual(new_book['author'], author)

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
