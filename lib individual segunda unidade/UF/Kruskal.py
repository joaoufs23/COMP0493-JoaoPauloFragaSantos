def kruskal(grafo):
    arestas = []
    for u in grafo:
        for v, peso in grafo[u]:
            arestas.append((peso, u, v))
    arestas.sort()
    uf = UniaoFind(len(grafo))
    arvore_minima = []
    for peso, u, v in arestas:
        if uf.unir(u, v):
            arvore_minima.append((u, v, peso))
    return arvore_minima
