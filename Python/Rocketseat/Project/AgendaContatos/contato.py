# Contato.py
class Contato:
    def __init__(self, nome, telefone, email, favorito=False):

        # Atributo para armazenar o nome do contato.
        self.nome = nome

        # Atributo para armazenar o número de telefone do contato.
        self.telefone = telefone

        # Atributo para armazenar o endereço de email do contato.
        self.email = email

        # Atributo para indicar se o contato é favorito ou não (o padrão é False).
        self.favorito = favorito
