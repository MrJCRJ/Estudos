import json

class Contato:
    def __init__(self, nome, telefone, email, favorito=False):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.favorito = favorito

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




agenda = Agenda()
agenda.carregar_contatos_de_arquivo('contatos.txt')

while True:
    print("\n1. Adicionar Contato")
    print("2. Visualizar Contatos")
    print("3. Editar Contato")
    print("4. Marcar/Desmarcar Favorito")
    print("5. Listar Favoritos")
    print("6. Apagar Contato")
    print("0. Sair")

    escolha = input("Escolha uma opção: ")
    
    
    if escolha == "0":
        agenda.salvar_contatos_em_arquivo('contatos.txt')
        break

    elif escolha == "1":
        nome = input("Nome: ").title()
        telefone = input("Telefone: ")
        email = input("Email: ")
        favorito = input("É favorito? (S/N): ").upper() == "S"
        novo_contato = Contato(nome, telefone, email, favorito)
        agenda.adicionar_contato(novo_contato)

    elif escolha == "2":
        agenda.visualizar_contatos()
        #formatar numero de telefone
        #queria poder aumentar o tamanho da estrela

    elif escolha == "3":
        agenda.visualizar_contatos()
        indice = int(input("Índice do contato a ser editado: ")) -1
        novo_nome = input("Novo nome: ").title()
        novo_telefone = input("Novo telefone: ")
        novo_email = input("Novo Email: ")
        novo_favorito = input("É favorito? (S/N): ").upper() == "S"
        novo_contato = Contato(novo_nome, novo_telefone, novo_email, novo_favorito)
        agenda.editar_contato(indice, novo_contato)

    elif escolha == "4":
        agenda.visualizar_contatos()
        indice = int(input("Índice do contato a ser marcado/desmarcado como favorito: ")) - 1
        agenda.marcar_desmarcar_favorito(indice)

    elif escolha == "5":
        agenda.listar_favoritos()

    elif escolha == "6":
        agenda.visualizar_contatos()
        indice = int(input("Índice do contato a ser apagado: ")) - 1
        agenda.apagar_contato(indice)

    else:
        print("Opção inválida. Tente novamente.")