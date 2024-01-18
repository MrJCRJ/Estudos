def adicionar_tarefas(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso")
    return

def menu():
    print("\n Menu do Gerenciador de Lista de Tarefas: ")
    print("1. Adicionar Tarefa")
    print("2. Ver Tarefas")
    print("3. Atualizar Tarefa")
    print("4. Completar Tarefa")
    print("5. Deletar Tarefas Completadas")
    print("0. Sair")

tarefas = []
while True:
    menu()

    escolha = input("Digite a sua escolha: ")

    if escolha == "0":
        break

    elif escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa deseja adicionar: ")
        adicionar_tarefas(tarefas, nome_tarefa)


print('Programa finalizado')