# estrutura-de-dados-api

## Objetivo
Implementar uma Rest API com endpoint separado para cada um dos métodos.

### Fila
- Inserir novo item na fila;
- Remover um item da fila;
- Imprimir a fila;

**Funcionamento da Fila:**

![image](https://user-images.githubusercontent.com/81869607/211394952-13604683-9e58-47ce-bba5-13736a871989.png)

[link](https://www.treinaweb.com.br/blog/o-que-e-e-como-funciona-a-estrutura-de-dados-fila)

### Pilha

- Inserir novo item na pilha;
- Remover um item da pilha;
- Imprimir a pilha;

**Funcionamento da Pilha:**

![image](https://user-images.githubusercontent.com/81869607/211394569-a1b3f8da-946d-43d5-8faf-775739ff3884.png)

[Link](https://www.treinaweb.com.br/blog/o-que-e-e-como-funciona-a-estrutura-de-dados-pilha#:~:text=Pilhas%20s%C3%A3o%20estruturas%20de%20dados,pilha%20quando%20precisarmos%20remov%C3%AA%2Dlo.)

## Quais são os requisitos minimos do projeto?

Todos os métodos devem ter testes unitarios.

## Dados
Os dados das pilhas e filas podem ser texto, números, objetos etc...

## Desenvolvimento

- Python3
- FlaskApi

```python
pip install flask
```

```python
#1. Objetivo - Criar uma api que disponibiliza a consulta, adição e exclusão de livros.

#2. URL base - localhost

#3. Endpoints fila:
  #-- localhost/fila/livros (GET)
  #-- localhost/fila/livros (POST)
  #-- localhost/fila/livros (DELETE)

#3. Endpoints pilha:
  #-- localhost/pilha/livros (GET)
  #-- localhost/pilha/livros (POST)
  #-- localhost/pilha/livros (DELETE)

#4. Quais recursos

```

![image](https://user-images.githubusercontent.com/81869607/211540328-1c702b8c-d61f-469c-acd0-ca5bef467d90.png)

# Construir uma Rest API com FlaskAPI

- [Link1](https://pythonbasics.org/flask-rest-api/)
- [Link2](https://www.geeksforgeeks.org/python-build-a-rest-api-using-flask/)

```python
# Imprimir todos os livros da pilha (GET)
# Adicionar livro na pilha (POST)
# Deletar livro da pilha (DELETE)
```

append -- > Adicionar um único elemento ao final de uma lista.

del -- > 

```python
my_api/
  app/
    controllers/
      users_controller.py
      products_controller.py
    models/
      users.py
      products.py
    routes/
      users.py
      products.py
  tests/
    controllers/
      test_users_controller.py
      test_products_controller.py
    models/
      test_users.py
      test_products.py
  config/
    config.py
  docs/
    api_docs.md
```

- A pasta app contém os arquivos relacionados à lógica da aplicação.
- A pasta controllers contém os arquivos responsáveis por lidar com as solicitações HTTP e chamar as operações dos modelos.
- A pasta models contém os arquivos responsáveis por lidar com as operações de banco de dados.
- A pasta routes contém os arquivos responsáveis por mapear as rotas da API para os controladores.
- A pasta tests contém os arquivos de teste para a aplicação.
- A pasta config contém arquivos de configuração para a aplicação.
- A pasta docs contém a documentação da API.

_____________________________________________________

1 - Rotas: as requisições HTTP são enviadas para as rotas, que determinam o endpoint da API.

2 - Controladores: as requisições são direcionadas aos controladores associados às rotas. Os controladores são responsáveis por processar a requisição e realizar as operações necessárias.

3 - Modelos: os controladores podem acessar os modelos para obter ou atualizar informações do banco de dados.

4 - Retorno da resposta: depois de processar a requisição, os controladores formatam a resposta e a enviam de volta ao cliente.

### Testes Unitários

> Testes de Rota:
*Verifica se as rotas estão funcionando corretamente e respondendo com o status correto e o corpo da resposta esperado.*

Utilizando a biblioteca unittest:

- Usamos o método setUp para instanciar a classe `BooksRepository` antes de cada teste. 
- Em seguida, definimos o teste unitário para a função de exemplo `delete_book`.
- Verificamos se o código de status retornado é 200 (sucesso) e se o título do livro deletado é igual ao título esperado.

### Adicionar mais dados na API e deixar ela mais completa

```python
class Livro:
    def __init__(self, titulo, autor, descricao, editora, data_publicacao, num_paginas, isbn, idioma, genero, imagem_capa):
        self.titulo = titulo
        self.autor = autor
        self.descricao = descricao
        self.editora = editora
        self.data_publicacao = data_publicacao
        self.num_paginas = num_paginas
        self.isbn = isbn
        self.idioma = idioma
        self.genero = genero
        self.imagem_capa = imagem_capa
```
### Códigos de status HTTP mais comuns

- 200 OK: A requisição foi bem sucedida.
- 201 Created: A requisição foi bem sucedida e um novo recurso foi criado como resultado.
- 204 No Content: A requisição foi bem sucedida, mas não há conteúdo para retornar (por exemplo, em uma requisição de exclusão).
- 400 Bad Request: A requisição não pôde ser entendida ou foi malformada.
- 401 Unauthorized: A autenticação falhou ou o usuário não tem permissão para acessar o recurso solicitado.
- 403 Forbidden: O servidor entende a requisição, mas se recusa a processá-la. Diferente do status 401, a autenticação não irá resolver o problema.
- 404 Not Found: O recurso solicitado não foi encontrado no servidor.
- 500 Internal Server Error: O servidor encontrou um erro inesperado que impediu a requisição de ser completada.


error handling python
json api response
json api response
https://jsonapi.org/

{
    data: {...}
    statusCode: 200,
    message: "Livro adicionado com sucesso"
}

padrão resposta api
- estudar tratamento de erro python
- escrever os testes da aplicação com mock

### Estrutura de pastas com testes:
```markdown
app/
├── __init__.py
├── controller/
│   ├── __init__.py
│   ├── example_controller.py
│   └── test_example_controller.py
├── models/
│   ├── __init__.py
│   ├── example_model.py
│   └── test_example_model.py
├── repository/
│   ├── __init__.py
│   ├── example_repository.py
│   └── test_example_repository.py
├── routes/
│   ├── __init__.py
│   ├── example_routes.py
│   └── test_example_routes.py
└── service/
    ├── __init__.py
    ├── example_service.py
    └── test_example_service.py
```

