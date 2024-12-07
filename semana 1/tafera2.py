def encontrar_indices(TTT, PPP):
    indices = []
    pos = TTT.find(PPP)
    while pos != -1:
        indices.append(pos)
        pos = TTT.find(PPP, pos + 1)
    if not indices:
        return -1
    return indices

TTT = "aqui é um exemplo de texto longo, apenas para teste do código"
PPP = "exemplo"
resultado = encontrar_indices(TTT, PPP)
print(resultado)
