class GrafoListaAdj:
    def __init__(self, vertices):
        self.vertices = vertices
        self.lista_adj = [[] for _ in range(vertices)]
    
    def adicionar_aresta(self, u, v):
        self.lista_adj[u].append(v)
        self.lista_adj[v].append(u)

    def dfs(self, inicio):
        visitado = [False] * self.vertices
        ordem = []
        
        def _dfs(v):
            visitado[v] = True
            ordem.append(v)
            for vizinho in self.lista_adj[v]:
                if not visitado[vizinho]:
                    _dfs(vizinho)

        _dfs(inicio)
        return ordem
