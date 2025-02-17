def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    meio = len(arr) // 2
    left = merge_sort(arr[:meio])
    right = merge_sort(arr[meio:])
    
    return merge(left, right)

def merge(left, right):
    sorted_array = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    
    while i < len(left):
        sorted_array.append(left[i])
        i += 1
    
    while j < len(right):
        sorted_array.append(right[j])
        j += 1
    
    return sorted_array

arr = [38, 27, 43, 3, 9, 82, 10]
resultado = merge_sort(arr)
print(f'Lista ordenada: {resultado}')
