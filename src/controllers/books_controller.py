from flask import Flask, jsonify, request
from models.books import Livro

app = Flask(__name__)

def iniciar_rotas():
  
  @app.route("/")
  def root():
    return "<h1>API em Flask<h1>"


  @app.route('/fila/livros', methods=['GET'])
  def obter_livros():
    return jsonify(livros)

  @app.route('/fila/livro', methods=['POST'])
  def adicionar_livros():
    body = request.get_json()
    
    ids = len(livros)
    if ids:
      new_id = ids + 1
    else:
      new_id = 1
      
    novo_livro = {
      "id": new_id,
      "título": body["título"],
      "autor": body["autor"]
    }

    livros.append(novo_livro)
    
    return jsonify(novo_livro)

  @app.route('/fila/livro', methods=['DELETE'])
  def excluir_livro():
    
    if not len(livros) == 0:
      del livros[0]
    
    return jsonify(livros)

