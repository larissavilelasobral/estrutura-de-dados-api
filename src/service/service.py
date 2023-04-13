import re
from src.controllers.books_controller import BooksRepository
from src.service.exceptions import InvalidCoverImageError


class BooksService:
    def __init__(self):
        self.books_repository = BooksRepository()

    def handle_book(self, body):
        try:
            title = body.get('title')
            author = self.clear_author_name(body.get('author'))
            description = self.check_description_length(body.get('description'))
            publisher = body.get('publisher')
            publication_date = body.get('publication_date')
            num_pages = body.get('num_pages')
            isbn = self.check_isbn_length(body.get('isbn'))
            language = self.check_language(body.get('language'))
            genre = body.get('genre')
            cover_image = self.check_cover_image(body.get('cover_image'))

            return self.books_repository.add_book(title, author, description, publisher, publication_date, num_pages,
                                                  isbn, language, genre, cover_image)
        except Exception as e:
            print(f'Error handling book: {str(e)}')
            return {'error': 'Could not handle book.'}, 500

    def clear_author_name(self, author_name):
        """
        remover caracteres especiais e números do nome do autor
        """
        return re.sub('[^a-zA-Z ]+', '', author_name)

    def check_description_length(self, description):
        """
        Receber descrição do livro e tratá-la para entrar no padrão de 250 caracteres.
        """
        max_length = 250
        if len(description) > max_length:
            raise ValueError(f"Descrição muito longa. O comprimento máximo permitido é de {max_length} caracteres.")
        return description

    def check_isbn_length(self, isbn):
        """
         Remover caracteres especiais e espaços em branco
        """
        isbn = re.sub('[^0-9]+', '', isbn)

        """
        Verificar se o ISBN possui 13 dígitos numéricos
        """
        if not isbn.isdigit() or len(isbn) != 13:
            error_message = f'Invalid ISBN: {isbn}'
            return {'error': error_message}, 400

        return isbn

    def check_language(self, language):
        """
        Verifica se o idioma do livro é uma string válida.
        """
        if not isinstance(language, str) or not language.strip():
            return {'error': f'Invalid language: {language}'}, 400
        return language

    def check_cover_image(self, cover_image_url):
        """
        Verifica se a URL da imagem da capa do livro é uma string válida.
        """
        if not isinstance(cover_image_url, str) or not cover_image_url.strip():
            raise InvalidCoverImageError(f'Invalid cover image URL: {cover_image_url}')
        return cover_image_url
