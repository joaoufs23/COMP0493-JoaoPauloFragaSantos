def mochila_fracionaria(pesos, valores, capacidade):
    n = len(pesos)
    itens = [(valores[i], pesos[i], i) for i in range(n)]
    
    itens.sort(key=lambda x: x[0] / x[1], reverse=True)

    valor_total = 0
    capacidade_restante = capacidade
    
    for valor, peso, idx in itens:
        if capacidade_restante == 0:
            break
        
        if peso <= capacidade_restante:
            capacidade_restante -= peso
            valor_total += valor
        else:
            valor_total += valor * (capacidade_restante / peso)
            capacidade_restante = 0
    
    return valor_total
