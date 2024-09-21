"""
    11.	Write a program to identify whether a string is a palindrome or not without 
        using reverse(), slicing
"""

str = input("Enter the String: ") 

str_2 = ""

for ch in str:
  str_2 = ch + str_2

if str == str_2:
  print(str, "is Palindrome")
else:
  print(str, "is not Palindrome")