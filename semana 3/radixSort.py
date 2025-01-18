def countingSort(myArray, posicao):
    if len(myArray) == 0:  # aqui estou olhando se a lista está vazia, se tiver, eu retorno a lista
        return myArray
    valorMaximo = max(myArray)  # aqui estou pegando o valor máximo e na outra linha o valor mínimo, já que é necessário
    valorMinimo = min(myArray)
    valorIntervalo = valorMaximo - valorMinimo + 1  # aqui estou criando as listas necessárias, e pegando o tamanho da lista
    listaDeContagem = [0] * 10 
    listaDeSaida = [0] * len(myArray)
    for num in myArray:
        listaDeContagem[(num // posicao) % 10] += 1
    for i in range(1, len(listaDeContagem)):
        listaDeContagem[i] += listaDeContagem[i - 1]
    for num in reversed(myArray):
        listaDeSaida[listaDeContagem[(num // posicao) % 10] - 1] = num
        listaDeContagem[(num // posicao) % 10] -= 1
    return listaDeSaida


def radixSort(myArray):
    valorMaximo = max(myArray)
    posicao = 1
    while valorMaximo // posicao > 0:
        myArray = countingSort(myArray, posicao)
        posicao *= 10
    return myArray
