class ArvoreSegmento:
    def __init__(self, dados):
        self.n = len(dados)
        self.tamanho = 1
        while self.tamanho < self.n:
            self.tamanho <<= 1
        self.min = [float('inf')] * (2 * self.tamanho)
        self.max = [-float('inf')] * (2 * self.tamanho)
        self.soma = [0] * (2 * self.tamanho)
        
        for i in range(self.n):
            self.min[self.tamanho + i] = dados[i]
            self.max[self.tamanho + i] = dados[i]
            self.soma[self.tamanho + i] = dados[i]
        
        for i in range(self.tamanho - 1, 0, -1):
            self.min[i] = min(self.min[2 * i], self.min[2 * i + 1])
            self.max[i] = max(self.max[2 * i], self.max[2 * i + 1])
            self.soma[i] = self.soma[2 * i] + self.soma[2 * i + 1]
    
    def atualizar_ponto(self, pos, valor):
        pos += self.tamanho
        self.min[pos] = self.max[pos] = self.soma[pos] = valor
        pos >>= 1
        while pos >= 1:
            self.min[pos] = min(self.min[2 * pos], self.min[2 * pos + 1])
            self.max[pos] = max(self.max[2 * pos], self.max[2 * pos + 1])
            self.soma[pos] = self.soma[2 * pos] + self.soma[2 * pos + 1]
            pos >>= 1
    
    def atualizar_intervalo(self, l, r, valor):
        pass
    
    def consulta_soma(self, l, r):
        res = 0
        l += self.tamanho
        r += self.tamanho
        while l <= r:
            if l % 2 == 1:
                res += self.soma[l]
                l += 1
            if r % 2 == 0:
                res += self.soma[r]
                r -= 1
            l >>= 1
            r >>= 1
        return res
    
    def consulta_min(self, l, r):
        res = float('inf')
        l += self.tamanho
        r += self.tamanho
        while l <= r:
            if l % 2 == 1:
                res = min(res, self.min[l])
                l += 1
            if r % 2 == 0:
                res = min(res, self.min[r])
                r -= 1
            l >>= 1
            r >>= 1
        return res
    
    def consulta_max(self, l, r):
        res = -float('inf')
        l += self.tamanho
        r += self.talho
        while l <= r:
            if l % 2 == 1:
                res = max(res, self.max[l])
                l += 1
            if r % 2 == 0:
                res = max(res, self.max[r])
                r -= 1
            l >>= 1
            r >>= 1
        return res
