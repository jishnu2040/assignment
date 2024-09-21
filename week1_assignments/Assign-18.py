"""
    18. Write a program to print the following pattern using for loop
        7 8 9 10 
        4 5 6
        2 3
        1
"""

rows = 4
num = 7

i = rows
while i >= 1:
  temp = num
  j = 1
  while j <= i:
     print(" ", temp, end = "")
     temp += 1
     j += 1
  print()
  num -= (i - 1)
  i -= 1
          
