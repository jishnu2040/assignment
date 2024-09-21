"""
    7.	Write a program to print the multiplication table of given numbers. 
        Using for and while
"""



def multiplication_for_loop(num, limit):
  for i in range(limit+1):
    if i != 0:
      result = i * num
      print(i, "*", num, " = ", result)


def multiplication_while_loop(num, limit):
  i = 1
  while i <= limit:
    result = i * num
    print(i, "*", num, " = ", result)
    i += 1

num = int(input("Enter a Number: "))

print("Multiplication Table of ", num, "using FOR Loop")
multiplication_for_loop(num, 10)

print("Multiplication Table of ", num, "using WHILE Loop")
multiplication_while_loop(num, 10)



