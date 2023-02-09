import uuid


class Book:
    def __init__(self, title, author):
        self.id = str(uuid.uuid4())
        self.title = title
        self.author = author
