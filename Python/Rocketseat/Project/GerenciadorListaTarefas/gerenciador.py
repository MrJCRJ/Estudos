def adicionar_tarefas(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso")
    return

def ver_tarefas(tarefas):
    print("\nLista de Tarefas:")
    for indice, tarefa in enumerate(tarefas, start=1):
        status =  "✓" if tarefa["completado"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")
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

    elif escolha == "2":
        ver_tarefas(tarefas)
    elif escolha == "3":
        pass
    elif escolha == "4":
        pass
    elif escolha == "5":
        pass


print('Programa finalizado')