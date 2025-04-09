def busca_kmp(texto, padrao):
    def calcular_vetor_lps(padrao):
        lps = [0] * len(padrao)
        comprimento = 0
        i = 1
        while i < len(padrao):
            if padrao[i] == padrao[comprimento]:
                comprimento += 1
                lps[i] = comprimento
                i += 1
            else:
                if comprimento != 0:
                    comprimento = lps[comprimento - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = calcular_vetor_lps(padrao)
    i = j = 0
    ocorrencias = []
    while i < len(texto):
        if texto[i] == padrao[j]:
            i += 1
            j += 1
            if j == len(padrao):
                ocorrencias.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return ocorrencias
