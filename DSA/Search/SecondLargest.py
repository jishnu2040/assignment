arr = [22, 3, 13, 31, 11,2, 19]

# used bubble sort technique 
for i in range(2):
    for j in range(i+1,len(arr)):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
print(arr[-2])