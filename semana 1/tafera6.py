def contar_ultima_linha(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        linhas = f.readlines()
        for i in range(len(linhas)):
            if linhas[i].startswith("......."):
                ultima_linha = linhas[i + 1].strip()  
                return len(ultima_linha)
    return 0  

nome_arquivo = "exemplo.txt" 
resultado = contar_ultima_linha(nome_arquivo)
print(f"A última linha tem {resultado} caracteres.")
