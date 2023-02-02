from flask import Flask
from src.routes.routes import books

app = Flask(__name__)
app.register_blueprint(books)

if __name__ == '__main__':
    PORT = 5000
    app.run(port=PORT, host='localhost', debug=True)
