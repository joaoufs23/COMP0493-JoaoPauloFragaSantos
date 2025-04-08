class UniaoFind:
    def __init__(self, tamanho):
        self.pai = list(range(tamanho))
        self.rank = [0] * tamanho

    def encontrar(self, x):
        if self.pai[x] != x:
            self.pai[x] = self.encontrar(self.pai[x])
        return self.pai[x]

    def unir(self, x, y):
        raiz_x = self.encontrar(x)
        raiz_y = self.encontrar(y)
        if raiz_x == raiz_y:
            return False
        if self.rank[raiz_x] > self.rank[raiz_y]:
            self.pai[raiz_y] = raiz_x
        else:
            self.pai[raiz_x] = raiz_y
            if self.rank[raiz_x] == self.rank[raiz_y]:
                self.rank[raiz_y] += 1
        return True
