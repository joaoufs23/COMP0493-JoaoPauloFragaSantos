def problema_do_troco(valor, moedas):
    moedas.sort(reverse=True)
    troco = []
    
    for moeda in moedas:
        while valor >= moeda:
            valor -= moeda
            troco.append(moeda)
    
    return troco
