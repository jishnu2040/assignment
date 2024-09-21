"""
    9.	Write a program to create a copy of array and add an element to copied 
        array. show both arrays.
        a.	Program should accept an array from the user, swap the values of 2 arrays 
            and display it on the console
"""
def copy_array(array):
  copy = array[:]
  return copy

array1 = []

size_arr_1 = int(input("Enter the Size of 1st Array: "))

print("Enter the Elements of 1st Array: ")
for i in range(size_arr_1):
  num = int(input())
  array1.insert(i, num)

print("\nArray 1: ", array1)

array2 = copy_array(array1)

ch = "y"

while ch == "y" or ch == "Y":
  num = int(input("\nEnter the New Elements of 2nd Array: "))
  array2.append(num)
  ch = input("\nDo you want to enter another element ? (Y/N) ")
  
print("\nArray 2: ", array2)




