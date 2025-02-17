def read_file(name_file):
    with open(name_file, 'r') as f:
        texto_final = []
        for linha in f:
            if linha.startswith("......."):
                break
            texto_final.append(linha.strip())
        return " ".join(texto_final)

nome_arquivo = "exemplo.txt"
resultado = read_file(nome_arquivo)
print(resultado)
