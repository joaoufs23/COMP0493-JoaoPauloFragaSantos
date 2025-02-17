def escalonamento_tarefas(tarefas):
    tarefas.sort(key=lambda x: x[1])
    
    tempo_atual = 0
    for tarefa in tarefas:
        tempo_atual += tarefa[0]
        if tempo_atual > tarefa[1]:
            print(f"Tarefa {tarefa} não pode ser executada a tempo!")
