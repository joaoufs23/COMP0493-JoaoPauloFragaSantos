def busca_rabin_karp(texto, padrao, primo=101):
    d = 256
    n = len(texto)
    m = len(padrao)
    h = pow(d, m - 1, primo)
    p = 0
    t = 0
    ocorrencias = []

    for i in range(m):
        p = (d * p + ord(padrao[i])) % primo
        t = (d * t + ord(texto[i])) % primo

    for deslocamento in range(n - m + 1):
        if p == t:
            correspondencia = True
            for i in range(m):
                if padrao[i] != texto[deslocamento + i]:
                    correspondencia = False
                    break
            if correspondencia:
                ocorrencias.append(deslocamento)
        if deslocamento < n - m:
            t = (d * (t - ord(texto[deslocamento]) * h) + ord(texto[deslocamento + m])) % primo
            if t < 0:
                t += primo
    return ocorrencias
