import re

def dividir_em_tokens(TTT):
    tokens = re.split('[ .]+', TTT)
    return [token for token in tokens if token]

TTT = "aqui é um exemplo de texto longo, apenas para teste do código. Porém, dessa vez tem espaços e pontos como solicitado"
tokens = dividir_em_tokens(TTT)
print(tokens)
