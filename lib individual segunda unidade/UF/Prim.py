import heapq

def prim(grafo, inicio=0):
    arvore_minima = []
    visitados = set()
    heap = []
    heapq.heappush(heap, (0, inicio, None))

    while heap:
        peso, u, pai = heapq.heappop(heap)
        if u in visitados:
            continue
        visitados.add(u)
        if pai is not None:
            arvore_minima.append((pai, u, peso))
        for v, w in grafo[u]:
            if v not in visitados:
                heapq.heappush(heap, (w, v, u))
    return arvore_minima
