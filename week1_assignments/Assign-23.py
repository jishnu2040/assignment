"""
    23. Write a function to calculate the sum of all numbers passed as its arguments. Your function should be 
        called sum_numbers and should define a single variable argument (i.e. a star argument) that will get the 
        values to sum.
"""

def sum_numbers(*a):
  sum = 0
  for i in a:
    sum = sum + i
  print(sum)
    
sum_numbers(1,2,3)
sum_numbers(8,20,2)
sum_numbers(12.5,3.147,98.2)
sum_numbers(1.1,2.2,5.5)