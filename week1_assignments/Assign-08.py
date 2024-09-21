"""
    8.	Write a program to print the following pattern (hint: use nested loop)
        1
        1 2
        1 2 3
        1 2 3 4
        1 2 3 4 5
"""

i = 1
limit = 5

while i <= limit:
  j = 1
  while j <= i:
    print(j, end = " ")
    j += 1
  print()
  i += 1
