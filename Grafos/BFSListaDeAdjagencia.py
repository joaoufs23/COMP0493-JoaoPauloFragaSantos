from collections import deque

class GrafoListaAdj:
    def __init__(self, vertices):
        self.vertices = vertices
        self.lista_adj = [[] for _ in range(vertices)]
    
    def adicionar_aresta(self, u, v):
        self.lista_adj[u].append(v)
        self.lista_adj[v].append(u)

    def bfs(self, inicio):
        visitado = [False] * self.vertices
        fila = deque([inicio])
        visitado[inicio] = True
        ordem = []

        while fila:
            v = fila.popleft()
            ordem.append(v)

            for vizinho in self.lista_adj[v]:
                if not visitado[vizinho]:
                    fila.append(vizinho)
                    visitado[vizinho] = True
        return ordem
