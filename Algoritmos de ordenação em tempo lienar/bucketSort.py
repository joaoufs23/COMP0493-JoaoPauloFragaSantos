def bucketSort(myArray):
    valorMaximo = max(myArray)
    lenLista = len(myArray)
    buckets = [[] for _ in range(lenLista)]
    
    for n in myArray:
        indice = int(n * lenLista / (valorMaximo + 1))
        buckets[indice].append(n)
    for i in range(lenLista):
        buckets[i].sort()
    arrayFinalizado = []
    for bucket in buckets:
        arrayFinalizado.extend(bucket)
    
    return arrayFinalizado
