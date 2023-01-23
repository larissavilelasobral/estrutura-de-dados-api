from flask import Flask
from controllers.books_controller import iniciar_rotas

app = Flask(__name__)

# criar uma classe com todos os metodos(com testes)

iniciar_rotas()

PORT = 5000
app.run(port=PORT,host='localhost', debug=True)