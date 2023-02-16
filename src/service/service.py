import re
# middleware
# service
# handler
# handler

# tratar as informações
# uma função faz uma ação de remover caracteres especiais e outra apenas avisa que o tamanho
# está incorreto. isso ta certo?


class BooksService:
    def __init__(self):
        pass

    def clear_author_name(self, name):
        """
        remover caracteres especiais e números do nome do autor
        """
        return re.sub('[^a-zA-Z ]+', '', name)

    def check_description_length(self, description, max_length):
        """
        Receber descrição do livre e trata-la para entrar no padrão de 250 caracteres.
        """
        if len(description) > max_length:
            description = description[:max_length]
            print(f'Descrição muito longa, ela foi cortada para {max_length} caracteres.')
        return description

    def check_isbn_length(self, isbn):
        """
        :param isbn:
        :return:
        """
        if len(isbn) != 13:
            return print({'error': f'Invalid ISBN: {isbn}'}), 400
        return isbn


