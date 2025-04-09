class ArvoreFenwick:
    def __init__(self, tamanho):
        self.n = tamanho
        self.arvore = [0] * (self.n + 1)
    
    def construir(self, arr):
        for i in range(self.n):
            self.atualizar(i, arr[i])
    
    def atualizar(self, indice, delta):
        indice += 1
        while indice <= self.n:
            self.arvore[indice] += delta
            indice += indice & -indice
    
    def consulta(self, indice):
        """Soma prefixo [0..índice]"""
        res = 0
        indice += 1
        while indice > 0:
            res += self.arvore[indice]
            indice -= indice & -indice
        return res
    
    def consulta_intervalo(self, l, r):
        """Soma do intervalo [l..r]"""
        return self.consulta(r) - self.consulta(l - 1)