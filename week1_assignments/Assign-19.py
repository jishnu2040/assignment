"""
    19. Write a program to add the values of two 2D arrays
        a.	Program should contain a class, Functions should be inside the class
"""

class ArrayAddition:
  
  def get_array(self):

    global arr1
    arr1 = []
    global arr2
    arr2 = []
    global size

    size = int(input("Enter the size of the array : "))

    print("Enter the Elements of 1st array: ")
    for i in range(size):
      temp = []
      for j in range(size):
        num = int(input())
        temp.append(num)
      arr1.append(temp)
         
    print("Enter the Elements of 2nd array: ")
    for i in range(size):
      temp = []
      for j in range(size):
        num = int(input())
        temp.append(num)
      arr2.append(temp)
     
  def add_array(self):
     
    global sum
    sum = [] * len(arr1)
 
    for i in range(size):
      temp = []
      for j in range(size):
        num = arr1[i][j] + arr2[i][j]
        temp.append(num)
      sum.append(temp)

  def display_array(self):   
    print("Sum of 2 arrays is:")
    for i in range(size):
      for j in range(size):
        print(sum[i][j], end=" ")
      print()
 
 
array_data = ArrayAddition()
 
array_data.get_array()
array_data.add_array()
array_data.display_array()
