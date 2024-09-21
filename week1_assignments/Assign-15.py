"""
    15. Write a program to accept an array and display it on the console 
        using functions
        a.	Program should contain 3 functions including main() function
            main()
                1.	Declare an array
                2.	Call function getArray()
                3.	Call function displayArray()
		    getArray()
                1.	Get values to the array
		    displayArray()
                1.	Display the array values
"""
def get_array():
  
  for i in range(size):
    ele = int(input())
    array.append(ele)
  return array

def display_array():
  
  for i in range(size):
    print(" ", array[i], end=" ")

def main():
  
  global array
  global size
  
  array=[]
  
  size=int(input("Enter the Size: "))
    
  print("Enter the Array Elements: ")
  get_array()

  print("Array: ")
  display_array()

main()