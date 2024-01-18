def adicionar_tarefas(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso")
    

def ver_tarefas(tarefas):
    print("\nLista de Tarefas:")
    for indice, tarefa in enumerate(tarefas, start=1):
        status =  "✓" if tarefa["completado"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")
    
def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    indece_tarefa_ajustado = indece_tarefa - 1
    if indece_tarefa_ajustado >= 0 and indece_tarefa_ajustado < len(tarefas):
        tarefas[indece_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
        print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}")
    else:
        print("Indeci de tarefa invalido! ")

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
        ver_tarefas(tarefas)
        indece_tarefa = input("Digite o número da tarefa que deseja atualizar: ")
        novo_nome = input("Digite o novo nome da tarefa: ")
        atualizar_nome_tarefa(tarefas, indece_tarefa, novo_nome)

    elif escolha == "4":
        pass
    elif escolha == "5":
        pass


print('Programa finalizado')