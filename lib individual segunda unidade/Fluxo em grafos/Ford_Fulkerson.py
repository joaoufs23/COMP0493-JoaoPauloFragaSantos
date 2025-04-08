def ford_fulkerson(grafo, origem, destino):
    grafo_residual = {u: {v: grafo[u][v] for v in grafo[u]} for u in grafo}
    fluxo_maximo = 0

    def dfs(u, fluxo, visitados):
        if u == destino:
            return fluxo
        visitados.add(u)
        for v in grafo_residual[u]:
            if v not in visitados and grafo_residual[u][v] > 0:
                fluxo_caminho = dfs(v, min(fluxo, grafo_residual[u][v]), visitados)
                if fluxo_caminho > 0:
                    grafo_residual[u][v] -= fluxo_caminho
                    grafo_residual[v][u] += fluxo_caminho  # Aresta reversa
                    return fluxo_caminho
        return 0

    while True:
        fluxo = dfs(origem, float('inf'), set())
        if fluxo == 0:
            break
        fluxo_maximo += fluxo

    return fluxo_maximo
