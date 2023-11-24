def mostrar_tarefas(tarefas):
    print("Tarefas:")
    for task_id, (descricao, concluida) in tarefas.items():
        marcador = "[x]" if concluida else "[ ]"
        print(f"{task_id}. {descricao} {marcador}")

def adicionar_tarefa(tarefas, descricao):
    task_id = len(tarefas) + 1
    tarefas[task_id] = (descricao, False)
    print(f"Tarefa '{descricao}' adicionada com ID {task_id}")

def marcar_como_concluida(tarefas, task_id):
    if task_id in tarefas:
        tarefas[task_id] = (tarefas[task_id][0], True)
        print(f"Tarefa {task_id} marcada como concluída.")
    else:
        print(f"Tarefa {task_id} não encontrada.")

# Exemplo de uso
tarefas = {}

adicionar_tarefa(tarefas, "Preparar a marmita")
adicionar_tarefa(tarefas, "Arrumar a mochila")
adicionar_tarefa(tarefas, "Fechar as janelas")

marcar_como_concluida(tarefas, 1)

mostrar_tarefas(tarefas)
