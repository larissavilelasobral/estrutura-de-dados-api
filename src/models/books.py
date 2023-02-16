import uuid


class Book:
    def __init__(self, title, author, description, publisher, publication_date, num_pages, isbn, language, genre, cover_image):
        self.id = str(uuid.uuid4())
        self.title = title
        self.author = author
        self.description = description
        self.publisher = publisher
        self.publication_date = publication_date
        self.num_pages = num_pages
        self.isbn = isbn
        self.language = language
        self.genre = genre
        self.cover_image = cover_image

