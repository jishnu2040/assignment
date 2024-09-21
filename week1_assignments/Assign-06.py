"""
    6.	Using the ‘switch case’ write a program to accept an input number from the user and output the day as follows. 

Input	1       2       3       4           5           6       7           Any other input
Output  Sunday  Monday  Tuesday Wednesday   Thursday    Friday  Saturday    Invalid Entry
"""

num = int(input("Enter a Number: "))

match (num):
  case 1: print("Sunday")
  case 2: print("Monday")
  case 3: print("Tuesday")
  case 4: print("Wednesday")
  case 5: print("Thursday")
  case 6: print("Friday")
  case 7: print("Saturday")
  case other: print("Invalid Entry")