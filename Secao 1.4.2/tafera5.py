from collections import Counter
import re

def palavra_mais_frequente(TTT):
    palavras = re.findall(r'\b\w+\b', TTT.lower())
    contagem = Counter(palavras)
    palavra, frequencia = contagem.most_common(1)[0]
    return palavra, frequencia

TTT = "Exemplo de texto, texto exemplo, texto."
palavra, frequencia = palavra_mais_frequente(TTT)
print(f"A palavra mais frequente é '{palavra}' e aparece {frequencia} vezes.")
