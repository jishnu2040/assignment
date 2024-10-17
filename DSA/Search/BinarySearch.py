def BinarySearch(arr, target):
    left = 0
    right = len(arr)-1
    
    while left < right:
        mid = left + right
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid -1
    return -1
        

arr = [12, 23, 45, 56, 67, 78, 88, 100]
target = 23
res = BinarySearch(arr, target)

if res == -1:
    print("element not found!!")
else:
    print(f'element found at {res+1} position!')
