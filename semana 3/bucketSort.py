def bucketSort(myArray):
    valorMaximo = max(myArray) # aqui eu esou pegando o maior valor da lista
    lenLista = len(myArray) # aqui eu estou pegando o tamanho da lista, para definir o número de buckets
    buckets = [[] for _ in range(lenLista)]
    
    for n in myArray:
        indice = int(n * lenLista / (valorMaximo + 1))
        buckets[indice].append(n)
    for i in range(lenLista):
        buckets[i].sort()
    arrayFinalizado = [] # essa parte aqui estou juntando em um único array
    for bucket in buckets:
        arrayFinalizado.extend(bucket)
    
    return arrayFinalizado
