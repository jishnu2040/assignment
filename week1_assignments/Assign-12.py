"""
    12.	Write a program to add to two dimensional arrays, understand the memory 
        management of list 
        a.	Program should accept two 2D arrays and display its sum
"""

def read_array(array_size):
  array = []
  for i in range(array_size):
    row_array = []
    for j in range(array_size):
      num = int(input())
      row_array.append(num)
    array.append(row_array)
  return array

array_size = int(input("Enter the Size of 2D Array: "))

print("\nEnter the Elements of 1st 2D Array: ")
array1 = read_array(array_size)

print("\nEnter the Elements of 2nd 2D Array: ")
array2 = read_array(array_size)

sum = []

for i in range(array_size):
  row_array = []
  for j in range(array_size):
    row_array.append(array1[i][j] + array2[i][j])
  sum.append(row_array)

print("\nResultant 2D Array: ")
for i in range(array_size):
  for j in range(array_size):
    print(" ", sum[i][j], end = "")
  print()


