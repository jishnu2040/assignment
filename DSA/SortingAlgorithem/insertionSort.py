def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j=i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr

arr = arr = [4, 22, 84, 1, 422, 2]
res = insertionSort(arr)
print(res)