# Agenda.py
import json
from contato import Contato
import os

class Agenda:
    # Inicializa a Agenda com uma lista vazia de contatos
    def __init__(self):
        self.contatos = []

    # Adiciona um novo contato à lista de contatos
    def adicionar_contato(self, contato):
        self.contatos.append(contato)
        print(f"Contato {contato.nome} adicionado com sucesso!")

    # Exibe todos os contatos na agenda
    def visualizar_contatos(self):
        print("\nLista de Contatos:\n")
        for indice, contato in enumerate(self.contatos, start=1):
            # Exibe informações do contato e marca com uma estrela se for favorito
            print(f"{indice}. {contato.nome} - {contato.telefone} - {contato.email} {'★' if contato.favorito else ''}")

    # Edita um contato na lista de contatos
    def editar_contato(self, indice, novo_contato):
        if 0 <= indice < len(self.contatos):
            self.contatos[indice] = novo_contato
            print(f"Contato {novo_contato.nome} editado com sucesso!")
        else:
            print("Erro: Índice inválido.")

    # Marca ou desmarca um contato como favorito
    def marcar_desmarcar_favorito(self, indice):
        self.contatos[indice].favorito = not self.contatos[indice].favorito
        print("Marcação feita com sucesso!")

    # Lista todos os contatos marcados como favoritos
    def listar_favoritos(self):
        print("\nLista de Favoritos:\n")
        favoritos = [contato for contato in self.contatos if contato.favorito]
        for indice, contato in enumerate(favoritos, start=1):
            print(f"{indice}. {contato.nome} - {contato.telefone} - {contato.email}")

    # Apaga um contato da lista de contatos
    def apagar_contato(self, indice):
        if 0 <= indice < len(self.contatos):
            nome_contato = self.contatos[indice].nome
            del self.contatos[indice]
            print(f"Contato {nome_contato} apagado com sucesso!")
        else:
            print("Erro: Índice inválido.")

    # Salva os contatos em um arquivo no formato JSON
    def salvar_contatos_em_arquivo(self, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            contatos_serializados = [vars(contato) for contato in self.contatos]
            json.dump(contatos_serializados, arquivo)
            print("Conta salva com sucesso!")

    # Carrega os contatos de um arquivo no formato JSON
    def carregar_contatos_de_arquivo(self, nome_arquivo):
        if os.path.exists(nome_arquivo):
            try:
                with open(nome_arquivo, 'r') as arquivo:
                    contatos_serializados = json.load(arquivo)
                    self.contatos = [Contato(**contato) for contato in contatos_serializados]
                    print("Carregamento concluido com sucesso!")
            except FileNotFoundError:
                pass  # Ignora se o arquivo não existir
