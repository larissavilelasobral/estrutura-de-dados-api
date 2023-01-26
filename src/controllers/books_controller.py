from flask import jsonify, request
from repository.books_repository import livros

def root():
    return "<h1>API em Flask<h1>"

def get_books():
    return jsonify(livros)

def add_book():
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
    
    return jsonify(livros)

def remove_book():
    if not len(livros) == 0:
        del livros[0]
    
    return jsonify(livros)
  
