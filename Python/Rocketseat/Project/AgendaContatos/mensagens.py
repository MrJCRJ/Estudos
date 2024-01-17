def exibir_mensagem_sucesso(mensagem):
    print(f"Sucesso: {mensagem}")

def exibir_mensagem_erro(mensagem):
    print(f"Erro: {mensagem}")

class ErroValidacao(Exception):
    pass