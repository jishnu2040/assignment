"""
    10.	 Write a program to sort an array in descending order without sort() 
    and sorted() Program should accept and array, sort the array values in 
    descending order and display it
"""
array = []

size_array = int(input("Enter the Size of 1st Array: "))

print("Enter the Elements of 1st Array: ")
for i in range(size_array):
  num = int(input())
  array.insert(i, num)

#Selection Sort
for i in range(0,size_array):
  max_pos = i
  for j in range(i+1, size_array):
    if array[j] > array[max_pos]:
      max_pos = j
  if max_pos != i:
    array[i],array[max_pos] = array[max_pos],array[i]

print("Sorted Array: ", array)