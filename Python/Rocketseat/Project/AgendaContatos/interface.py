from agenda import Agenda
from contato import Contato

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