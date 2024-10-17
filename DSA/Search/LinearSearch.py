def LinearSearch(arr, target):
    for i in range(len(arr)-1):
        if arr[i] == target:
            return i
        
    return -1



arr = [43, 53, 2, 90, 23, 324, 23, 982]

target = 232

result = LinearSearch(arr, target)

if result == -1:
    print("element not present in array")
else:
    print(f'element found at {result+ 1} position')