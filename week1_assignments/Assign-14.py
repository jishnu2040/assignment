"""
    14.  Write a program using user defined functions and lambda functions

"""




def add_numbers(num1, num2): # user defined function to perform addition
  sum = num1 + num2
  return sum

number1 = int(input ("Enter the 1st Number: "))
number2 = int(input ("Enter the 2nd Number: "))

result = add_numbers(number1, number2) 
print("The sum of two numbers is ", result)


summation = lambda num1, num2: num1 + num2 # lambada function

number1 = int(input ("\nEnter the 1st Number: "))
number2 = int(input ("Enter the 2nd Number: "))

result = summation(number1, number2)
print("The sum of two numbers is ", result)