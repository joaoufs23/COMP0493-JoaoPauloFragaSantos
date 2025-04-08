from collections import deque

def edmonds_karp(grafo, origem, destino):
    grafo_residual = {u: {v: grafo[u][v] for v in grafo[u]} for u in grafo}
    fluxo_total = 0

    while True:
        pais = {}
        fila = deque([origem])
        pais[origem] = None
        caminho_encontrado = False

        while fila and not caminho_encontrado:
            u = fila.popleft()
            for v in grafo_residual[u]:
                if v not in pais and grafo_residual[u][v] > 0:
                    pais[v] = u
                    if v == destino:
                        caminho_encontrado = True
                        break
                    fila.append(v)

        if not caminho_encontrado:
            break

        fluxo_caminho = float('inf')
        v = destino
        while v != origem:
            u = pais[v]
            fluxo_caminho = min(fluxo_caminho, grafo_residual[u][v])
            v = u

        v = destino
        while v != origem:
            u = pais[v]
            grafo_residual[u][v] -= fluxo_caminho
            grafo_residual[v][u] += fluxo_caminho
            v = u

        fluxo_total += fluxo_caminho

    return fluxo_total
