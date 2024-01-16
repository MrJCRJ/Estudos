from agenda import Agenda
from contato import Contato
import re

def validar_email(email):
    padrao_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(padrao_email, email) is not None

def validar_telefone(telefone):
    # Adapte este padrão conforme necessário para aceitar diferentes formatos de telefone
    padrão_telefone = r'^\d{11}$'
    return re.match(padrão_telefone, telefone) is not None

def validar_nome(nome):
    return all(caractere.isalpha() or caractere.isspace() for caractere in nome) and nome.strip() != ""
# Criando uma instância da classe Agenda
agenda = Agenda()

# Carregando contatos do arquivo 'contatos.txt'
agenda.carregar_contatos_de_arquivo('contatos.txt')

while True:
    # Exibindo o menu
    print("\n1. Adicionar Contato")
    print("2. Visualizar Contatos")
    print("3. Editar Contato")
    print("4. Marcar/Desmarcar Favorito")
    print("5. Listar Favoritos")
    print("6. Apagar Contato")
    print("0. Sair")

    # Solicitando a escolha do usuário
    escolha = input("Escolha uma opção: ")

    if escolha == "0":
        # Salvando contatos no arquivo 'contatos.txt' e encerrando o programa
        agenda.salvar_contatos_em_arquivo('contatos.txt')
        break

    elif escolha == "1":
        # Obtendo dados para adicionar um novo contato
        nome = input("Nome: ").title()
        while not validar_nome(nome):
            print("Erro: Por favor, insira um nome válido.")
            nome = input("Nome: ").title()
        telefone = input("Telefone: ")
        while not validar_telefone(telefone):
            print("Erro: Por favor, insira um número de telefone válido.")
            telefone = input("Telefone: ")
        email = input("Email: ")
        while not validar_email(email):
            print("Erro: Por favor, insira um email válido.")
            email = input("Email: ")
        favorito = input("É favorito? (S/N): ").upper() == "S"
        novo_contato = Contato(nome, telefone, email, favorito)
        
        # Adicionando o novo contato à agenda
        agenda.adicionar_contato(novo_contato)

    elif escolha == "2":
        # Visualizando todos os contatos na agenda
        agenda.visualizar_contatos()

    elif escolha == "3":
        # Visualizando todos os contatos antes de editar
        agenda.visualizar_contatos()
        
        # Obtendo índice do contato a ser editado
        indice = int(input("Índice do contato a ser editado: ")) - 1
        
        # Obtendo novos dados para o contato
        novo_nome = input("Novo nome: ").title()
        while not validar_nome(novo_nome):
            print("Erro: Por favor, insira um nome válido.")
            novo_nome = input("Nome: ").title()
        novo_telefone = input("Novo telefone: ")
        while not validar_telefone(novo_telefone):
            print("Erro: Por favor, insira um número de telefone válido.")
            novo_telefone = input("Telefone: ")
        novo_email = input("Novo Email: ")
        while not validar_email(novo_email):
            print("Erro: Por favor, insira um email válido.")
            novo_email = input("Email: ")
        novo_favorito = input("É favorito? (S/N): ").upper() == "S"
        
        # Criando um novo contato com os dados atualizados
        novo_contato = Contato(novo_nome, novo_telefone, novo_email, novo_favorito)
        
        # Editando o contato na agenda
        agenda.editar_contato(indice, novo_contato)

    elif escolha == "4":
        # Visualizando todos os contatos antes de marcar/desmarcar como favorito
        agenda.visualizar_contatos()
        
        # Obtendo índice do contato a ser marcado/desmarcado como favorito
        indice = int(input("Índice do contato a ser marcado/desmarcado como favorito: ")) - 1
        
        # Marcando/desmarcando como favorito
        agenda.marcar_desmarcar_favorito(indice)

    elif escolha == "5":
        # Listando todos os contatos marcados como favoritos
        agenda.listar_favoritos()

    elif escolha == "6":
        # Visualizando todos os contatos antes de apagar
        agenda.visualizar_contatos()
        
        # Obtendo índice do contato a ser apagado
        indice = int(input("Índice do contato a ser apagado: ")) - 1
        
        # Apagando o contato da agenda
        agenda.apagar_contato(indice)

    else:
        print("Opção inválida. Tente novamente.")
