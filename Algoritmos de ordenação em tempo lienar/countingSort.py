def countingSort(myArray):
    if len(myArray) == 0:
        return myArray
    valorMaximo = max(myArray)
    valorMinimo = min(myArray)
    valorIntervalo = valorMaximo - valorMinimo + 1
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
