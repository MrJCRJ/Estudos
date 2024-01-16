class Contato:
    def __init__(self, nome, telefone, email, favorito=False):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.favorito = favorito

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)
    
    def visualizar_contatos(self):
        for i, contato in enumerate(self.contatos, start=1):
            print(f"{i}. {contato.nome} - {contato.telefone} - {contato.email} {'★' if contato.favorito else ''}")



agenda = Agenda()
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
        break

    elif escolha == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        favorito = input("É favorito? (S/N): ").upper() == "S"
        novo_contato = Contato(nome, telefone, email, favorito)
        agenda.adicionar_contato(novo_contato)

    elif escolha == "2":
        pass

    elif escolha == "3":
        pass

    elif escolha == "4":
        pass

    elif escolha == "5":
        pass

    elif escolha == "6":
        pass

    else:
        print("Opção inválida. Tente novamente.")