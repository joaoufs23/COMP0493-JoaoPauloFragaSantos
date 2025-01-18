def countingSort(myArray):
    if len(myArray) == 0: # aqui estou olhando se a lista está fazia, se tiver, eu retorno a lista
        return myArray
    valorMaximo = max(myArray) # aqui esou pegando o valor máximo e na outra linha o valor minimo, já que é necessário
    valorMinimo = min(myArray)
    valorIntervalo = valorMaximo - valorMinimo + 1 # aqui estou criando as listas necessárias, e pegando o tamanho da lista
    listaDeContagem = [0] * valorIntervalo
    listaDeSaida = [0] * len(myArray)
    
    for num in myArray:
        listaDeContagem[num - valorMinimo] += 1
    for i in range(1, len(listaDeContagem)):
        listaDeContagem[i] += listaDeContagem[i - 1]
    for num in reversed(myArray):
        listaDeSaida[listaDeContagem[num - valorMinimo] - 1] = num
        listaDeContagem[num - valorMinimo] -= 1
    
    return listaDeSaida
