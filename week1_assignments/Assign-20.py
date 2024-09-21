"""
    20. Write a program to include all the functionalities of a calculator using ABSTRACT class and abstract method. 
        All the methods (add, sub, mul, div) should be inside of abstract class. Abstract method definition should be 
        in another class. 
"""

from abc import ABC, abstractmethod

# creating abstract class
class Calculator(ABC):
  
  @abstractmethod
  def add(self):
    pass
  
  @abstractmethod
  def sub(self):
    pass
  
  @abstractmethod
  def mul(self):
    pass
  
  @abstractmethod
  def div(self):
    pass
 
# inheriting abstract class and giving implementation
class My_Calculator(Calculator):

  def add(self, num1, num2):
    result = num1 + num2
    return result
  
  def sub(self, num1, num2):
    result = num1 - num2
    return result
 
  def mul(self, num1, num2):
    result = num1 * num2
    return result
  
  def div(self, num1, num2):
    result = num1 / num2
    return result
 
calc = My_Calculator()

option = 0

while option != 5:
  print("\n1.Addition  \n2.Subtraction \n3.Multiplication \n4.Division \n5.Exit")
  option = int(input("Select Operation: "))

  num1 = int(input("Enter 1st Number: "))
  num2 = int(input("Enter 2nd Number: "))

  match(option):
    case 1:
      result = calc.add(num1, num2)
      print("Result: ", result)
    case 2:
      result = calc.sub(num1, num2)
      print("Result: ", result)
    case 3:
      result = calc.mul(num1, num2)
      print("Result: ", result)
    case 4:
      result = calc.div(num1, num2)
      print("Result: ", result)
    case 5:
      exit()
    case other:
      print("Invalid Operation")