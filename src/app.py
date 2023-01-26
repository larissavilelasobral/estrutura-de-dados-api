from flask import Flask
from controllers.books_controller import root, get_books, add_book, delete_book

app = Flask(__name__)

app.route("/")(root)
app.route('/queue/book', methods=['GET'])(get_books)
app.route('/queue/book', methods=['POST'])(add_book)
app.route('/queue/book', methods=['DELETE'])(delete_book)

if __name__ == '__main__':
    PORT = 5000
    app.run(port=PORT,host='localhost', debug=True)
