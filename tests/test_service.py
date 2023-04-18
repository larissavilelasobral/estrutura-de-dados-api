import pytest
from unittest.mock import MagicMock
from src.repository.books_repository import BooksRepository
from src.service.exceptions import InvalidCoverImageError
from src.service.service import BooksService


class TestBooksService:
    @pytest.fixture(autouse=True)
    def setup(self, mocker):
        # instancia a classe que representa o Banco
        self.books_repository = BooksRepository()
        # cria um objeto que simula o objeto books_db que simula o nosso Banco
        self.mock_db = mocker.patch.object(self.books_repository, "books_db")

    def test_handle_book(self):
        # instancia a classe que contem a lógica
        self.books_service = BooksService()
        # definir BooksRepository é a fonte dos dados do objeto BooksService.
        self.books_service.books_repository = self.books_repository

        # arrange
        body = {
            'title': 'TDD com Python: Siga o Bode dos Testes',
            'author': 'Harry J. W. Percival',
            'description': 'Este livro é uma referência essencial para qualquer programador que queira escrever código mais legível.',
            'publisher': 'Alta Books',
            'publication_date': '2010',
            'num_pages': '464',
            'isbn': '978-8576082675',
            'language': 'Português',
            'genre': 'Tecnologia/Programação',
            'cover_image': 'Sem Imagem',
        }
        # instancia a classe MagicMock, sendo um objeto de simulação de teste
        add_book_mock = MagicMock()
        # atribui a função add_book do objeto books_repository para receber o objeto de teste add_book_mock
        self.books_repository.add_book = add_book_mock

        # act
        self.books_service.handle_book(body)

        # assert
        # definiu os valores que espera receber como parametro
        add_book_mock.assert_called_once_with(
            'TDD com Python: Siga o Bode dos Testes',
            'Harry J. W. Percival',
            'Este livro é uma referência essencial para qualquer programador que queira escrever código mais legível.',
            'Alta Books',
            '2010',
            '464',
            '978-8576082675',
            'Português',
            'Tecnologia/Programação',
            'Sem Imagem'
        )

    def test_clear_author_name(self, books_service):
        author_name = "J0hN D03"
        expected_result = "JhN D"
        assert books_service.clear_author_name(author_name) == expected_result

    def test_check_description_length(self, books_service):
        """
        Testando descrição com menos de 250 caracteres
        """
        description = "Uma descrição curta"
        assert books_service.check_description_length(description) == description

        """
        Testando descrição com exatamente 250 caracteres
        """
        description = "a" * 250
        assert books_service.check_description_length(description) == description

        """
        Testando descrição com mais de 250 caracteres
        """
        description = "a" * 300
        expected_output = {'error': 'Descrição muito longa, ela foi cortada para 250 caracteres.'}
        assert books_service.check_description_length(description) == expected_output

    def test_check_isbn_length_valid(self, books_service):
        isbn = '978-0544003415'
        assert books_service.check_isbn_length(isbn) == isbn

    def test_check_isbn_length_invalid(self, books_service):
        isbn = '978-05440034'
        assert books_service.check_isbn_length(isbn) == ({'error': f'Invalid ISBN: {isbn}'}, 400)

    def test_check_language_valid(self, books_service):
        language = 'English'
        assert books_service.check_language(language) == language

    def test_check_language_invalid(self, books_service):
        language = ''
        assert books_service.check_language(language) == ({'error': f'Invalid language: {language}'}, 400)

    def test_check_cover_image_valid(self, books_service):
        cover_image_url = 'https://example.com/image.jpg'
        assert books_service.check_cover_image(cover_image_url) == cover_image_url

    def test_check_cover_image_invalid(self, books_service):
        cover_image_url = ''
        with pytest.raises(InvalidCoverImageError) as exc_info:
            books_service.check_cover_image(cover_image_url)
        assert str(exc_info.value) == f'Invalid cover image URL: {cover_image_url}'
