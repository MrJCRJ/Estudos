import json
from contato import Contato

class Agenda:
    # Criar um bloco de notas para deixar salvo no computador
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)
    
    def visualizar_contatos(self):
        for indece, contato in enumerate(self.contatos, start=1):
            print(f"{indece}. {contato.nome} - {contato.telefone} - {contato.email} {'★' if contato.favorito else ''}")
    
    def editar_contato(self, indice, novo_contato):
        self.contatos[indice] = novo_contato

    def marcar_desmarcar_favorito(self, indice):
        self.contatos[indice].favorito = not self.contatos[indice].favorito

    def listar_favoritos(self):
        favoritos = []
        for contato in self.contatos:
            if contato.favorito:
                favoritos.append(contato)
        for indice, contato in enumerate(favoritos, start=1):
            print(f"{indice}. {contato.nome} - {contato.telefone} - {contato.email}")

    def apagar_contato(self, indice):
        del self.contatos[indice]
    
    def salvar_contatos_em_arquivo(self, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            contatos_serializados = [vars(contato) for contato in self.contatos]
            json.dump(contatos_serializados, arquivo)
    
    def carregar_contatos_de_arquivo(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                contatos_serializados = json.load(arquivo)
                self.contatos = [Contato(**contato) for contato in contatos_serializados]
        except FileNotFoundError:
            pass  # Ignora se o arquivo não existir
