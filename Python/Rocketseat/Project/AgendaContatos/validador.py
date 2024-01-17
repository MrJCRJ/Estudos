import re
from mensagens import ErroValidacao

def validar_email(email):
    padrao_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(padrao_email, email) is not None

def validar_telefone(telefone):
    # Padrão mais flexível para aceitar diferentes formatos de telefone
    padrão_telefone = r'^\d{10,14}$'
    return re.match(padrão_telefone, telefone) is not None

def validar_nome(nome):
    if not all(caractere.isalpha() or caractere.isspace() for caractere in nome) or nome.strip() == "":
        raise ErroValidacao("Nome inválido")
    return True