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