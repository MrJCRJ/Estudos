def adicionar_tarefas():
    pass

def menu():
    print("\n Menu do Gerenciador de Lista de Tarefas: ")
    print("1. Adicionar Tarefa")
    print("2. Ver Tarefas")
    print("3. Atualizar Tarefa")
    print("4. Completar Tarefa")
    print("5. Deletar Tarefas Completadas")
    print("0. Sair")

while True:
    menu()

    escolha = input("Digite a sua escolha: ")

    if escolha == "0":
        break


print('Programa finalizado')