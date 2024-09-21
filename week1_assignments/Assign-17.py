"""
    17. Write a menu driven program to do the basic mathematical operations such as 
        addition, subtraction, multiplication and division (hint: use if else ladder 
        or switch)
        a.  Program should have 4 functions named 
            addition(), subtraction(), multiplication() and division()
        b.	Should create a class object and call the appropriate function as user 
            prefers in the main function
"""
class Operations:

  def addition(self):
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter the 2nd number: "))
    result = num1 + num2
    print("The result is ", result)
 
  def subtraction(self):
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter the 2nd number: "))
    result = num1 - num2
    print("The result is ", result)
 
  def multiplication(self):
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter the 2nd number: "))
    result = num1 * num2
    print("The result is ", result)
 
  def division(self):
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter the 2nd number: "))
    result = num1 / num2
    print("The result is ", result)
 
math_ops = Operations()

option = 0

while option != 5:
  print("\n1.Addition  \n2.Subtraction \n3.Multiplication \n4.Division \n5.Exit")
  option = int(input("Select Operation: "))

  match(option):
    case 1:
      math_ops.addition()
    case 2:
      math_ops.subtraction()
    case 3:
      math_ops.multiplication()
    case 4:
      math_ops.division()
    case 5:
      exit()
    case other:
      print("Invalid Operation")


