"""
    4.	Write a program to check whether a student has passed or failed in a subject after he or she enters their mark 
        (pass mark for a subject is 50 out of 100).
        a.	Program should accept an input from the user and output a message as “Passed” or “Failed”
"""

mark = float(input("Enter Students Mark (out of 100): "))

if mark >= 50.0:
  print("Passed")
else:
  print("Failed")