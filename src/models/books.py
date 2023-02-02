import uuid


# organização/estruturar banco
class Book:

    def __init__(self, title, author):
        self.id = uuid.uuid4()
        self.title = title
        self.author = author
