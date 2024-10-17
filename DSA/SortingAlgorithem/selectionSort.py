def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_indx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_indx]:
                min_indx = j
        arr[i], arr[min_indx] = arr[min_indx], arr[i]

    return arr

arr = [4, 22, 84, 1, 422, 2]

res = selectionSort(arr)
print(res)

        