def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0

    meio = len(arr) // 2
    left, left_inversions = count_inversions(arr[:meio])
    right, right_inversions = count_inversions(arr[meio:])

    merged, split_inversions = merge_and_count(left, right)

    total_inversions = left_inversions + right_inversions + split_inversions
    
    return merged, total_inversions

def merge_and_count(left, right):
    sorted_array = []
    i = j = 0
    inversions = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
            inversions += len(left) - i
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    
    return sorted_array, inversions

arr = [38, 27, 43, 3, 9, 82, 10]
_, total_inversions = count_inversions(arr)
print(f'Total de inversões: {total_inversions}')
