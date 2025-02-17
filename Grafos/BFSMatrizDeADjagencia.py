from collections import deque

class GrafoMatrizAdj:
    def __init__(self, vertices):
        self.vertices = vertices
        self.matriz = [[0 for _ in range(vertices)] for _ in range(vertices)]
    
    def adicionar_aresta(self, u, v):
        self.matriz[u][v] = 1
        self.matriz[v][u] = 1

    def bfs(self, inicio):
        visitado = [False] * self.vertices
        fila = deque([inicio])
        visitado[inicio] = True
        ordem = []

        while fila:
            v = fila.popleft()
            ordem.append(v)

            for i in range(self.vertices):
                if self.matriz[v][i] == 1 and not visitado[i]:
                    fila.append(i)
                    visitado[i] = True
        return ordem
