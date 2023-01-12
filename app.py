from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
  {
    'id': 1,
    'título': 'Código limpo: Habilidades práticas do Agile Software',
    'autor': 'Robert C. Martin'
  },
  {
    'id': 2,
    'título': 'Arquitetura limpa: O guia para estrutura de software',
    'autor': 'Robert C. Martin'
  },
  {
    'id': 3,
    'título': 'Microsserviços Prontos Para a Produção',
    'autor': 'Susan J. Fowler'
  },
  {
    'id': 4,
    'título': 'Domain-Driven Design: Atacando as complexidades do software',
    'autor': 'Eric Evans'
  },
  {
    'id': 5,
    'título': 'Refatoração: Aperfeiçoando o Design de Códigos',
    'autor': 'Martin Fowler'
  },
  {
    'id': 6,
    'título': 'O Programador Pragmático: De Aprendiz a Mestre',
    'autor': 'Andrew Hunt & David Thomas'
  },
  {
    'id': 7,
    'título': 'Entendendo Algoritmos: Um Guia Ilustrado Para Programadores',
    'autor': 'Aditya Y. Bhargava'
  },
  {
    'id': 8,
    'título': 'Estruturas de Dados e Algoritmos com JavaScript',
    'autor': 'Loiane Groner'
  },
  {
    'id': 9,
    'título': 'Aprendendo TypeScript: Melhore Suas Habilidades',
    'autor': 'Josh Goldberg'
  },
  {
    'id': 10,
    'título': 'Linux Eficiente na Linha de Comando',
    'autor': 'Daniel J. Barrett'
  },
]

# Imprimir todos os livros da fila (GET)
@app.route('/livros', methods=['GET'])
def obter_livros():
  return jsonify(livros)

# Adicionar livro na fila (POST)
@app.route('/livro', methods=['POST'])
def adicionar_livros():
  novo_livro = request.get_json()
  
  livros.append(novo_livro)
  
  return jsonify(livros)

# Deletar livro da fila (DELETE)
@app.route('/livro', methods=['DELETE'])
def excluir_livro():
  if not len(livros) == 0:
    del livros[0]
  
  return jsonify(livros)
 
app.run(port=5000,host='localhost', debug=True)