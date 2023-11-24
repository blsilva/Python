import json

def carregar_tarefas():
    try:
        with open("tarefas.json", "r") as arquivo:
            tarefas = json.load(arquivo)
        return tarefas
    except FileNotFoundError:
        return {}

def salvar_tarefas(tarefas):
    with open("tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo)

def mostrar_tarefas(tarefas):
    print("Tarefas:")
    for task_id, (descricao, concluida) in tarefas.items():
        marcador = "[x]" if concluida else "[ ]"
        print(f"{task_id}. {descricao} {marcador}")

def adicionar_tarefa(tarefas, descricao):
    if descricao[0].isupper():
        task_id = len(tarefas) + 1
        tarefas[task_id] = (descricao, False)
        print(f"Tarefa {task_id}. {descricao} [ ] registrada. Tarefa adicionada!!!")
    else:
        print("A descrição da tarefa deve começar com maiúscula.")

def marcar_como_realizada(tarefas, task_id):
    if task_id in tarefas and not tarefas[task_id][1]:
        tarefas[task_id] = (tarefas[task_id][0], True)
        print(f"Tarefa {task_id} movida para o início da lista e marcada como realizada.")
    elif task_id in tarefas and tarefas[task_id][1]:
        print(f"Tarefa {task_id} já estava concluída.")
    else:
        print(f"Tarefa {task_id} não encontrada.")

def editar_tarefa(tarefas, task_id, nova_descricao):
    if task_id in tarefas:
        status_atual = "[x]" if tarefas[task_id][1] else "[ ]"
        tarefas[task_id] = (nova_descricao, tarefas[task_id][1])
        print(f"Tarefa {task_id} editada: {task_id}. {nova_descricao} {status_atual}")
    else:
        print(f"Tarefa {task_id} não encontrada.")

def menu(tarefas):
    while True:
        print("\n--- Menu ToDoList ---")
        print("1. Listar Tarefas")
        print("2. Adicionar Tarefa")
        print("3. Marcar Tarefa como Realizada")
        print("4. Editar Tarefa")
        print("5. Sair")

        opcao = input("Escolha uma opção (1-5): ")

        if opcao == "1":
            mostrar_tarefas(tarefas)
        elif opcao == "2":
            nova_tarefa_descricao = input("Digite a descrição da nova tarefa: ")
            adicionar_tarefa(tarefas, nova_tarefa_descricao)
        elif opcao == "3":
            tarefa_a_marcar_como_realizada = int(input("Digite o ID da tarefa a marcar como realizada: "))
            marcar_como_realizada(tarefas, tarefa_a_marcar_como_realizada)
        elif opcao == "4":
            tarefa_a_editar = int(input("Digite o ID da tarefa a editar: "))
            nova_descricao_tarefa = input("Digite a nova descrição da tarefa: ")
            editar_tarefa(tarefas, tarefa_a_editar, nova_descricao_tarefa)
        elif opcao == "5":
            salvar_tarefas(tarefas)
            print("Saindo do aplicativo ToDoList. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

tarefas = carregar_tarefas()

menu(tarefas)
