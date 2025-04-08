def busca_boyer_moore(texto, padrao):
    def heuristica_caracter_invalido(padrao):
        caracter_invalido = {}
        for i in range(len(padrao)):
            caracter_invalido[padrao[i]] = i
        return caracter_invalido

    caracter_invalido = heuristica_caracter_invalido(padrao)
    n = len(texto)
    m = len(padrao)
    ocorrencias = []
    deslocamento = 0
    while deslocamento <= n - m:
        j = m - 1
        while j >= 0 and padrao[j] == texto[deslocamento + j]:
            j -= 1
        if j < 0:
            ocorrencias.append(deslocamento)
            deslocamento += (m - caracter_invalido.get(texto[deslocamento + m], -1)) if deslocamento + m < n else 1
        else:
            deslocamento += max(1, j - caracter_invalido.get(texto[deslocamento + j], -1))
    return ocorrencias
