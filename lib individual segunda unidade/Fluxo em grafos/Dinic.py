from collections import deque

def dinic(grafo, origem, destino):
    grafo_residual = {u: {v: grafo[u][v] for v in grafo[u]} for u in grafo}
    fluxo_total = 0
    INF = float('inf')

    def bfs_grafo_nivel():
        nivel = {u: -1 for u in grafo_residual}
        nivel[origem] = 0
        fila = deque([origem])
        while fila:
            u = fila.popleft()
            for v in grafo_residual[u]:
                if nivel[v] == -1 and grafo_residual[u][v] > 0:
                    nivel[v] = nivel[u] + 1
                    fila.append(v)
        return nivel

    def dfs_fluxo_bloqueante(u, fluxo, nivel, ponteiro):
        if u == destino:
            return fluxo
        while ponteiro[u] < len(adj[u]):
            v = adj[u][ponteiro[u]]
            if nivel[v] == nivel[u] + 1 and grafo_residual[u][v] > 0:
                fluxo_caminho = dfs_fluxo_bloqueante(v, min(fluxo, grafo_residual[u][v]), nivel, ponteiro)
                if fluxo_caminho > 0:
                    grafo_residual[u][v] -= fluxo_caminho
                    grafo_residual[v][u] += fluxo_caminho
                    return fluxo_caminho
            ponteiro[u] += 1
        return 0

    adj = {u: list(grafo_residual[u]) for u in grafo_residual}

    while True:
        nivel = bfs_grafo_nivel()
        if nivel[destino] == -1:
            break
        ponteiro = {u: 0 for u in grafo_residual}
        while True:
            fluxo = dfs_fluxo_bloqueante(origem, INF, nivel, ponteiro)
            if fluxo == 0:
                break
            fluxo_total += fluxo

    return fluxo_total
