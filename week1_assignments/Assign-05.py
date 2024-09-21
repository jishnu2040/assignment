"""
    5.  Write a program to show the grade obtained by a student after he/she enters 
    their total mark percentage.
"""

mark_percent = float(input("Enter Students Total Mark Percentage (out of 100): "))

if mark_percent >= 90:
  print("Grade: A")
elif mark_percent >=80 and mark_percent<90:
  print("Grade: B")
elif mark_percent >=70 and mark_percent<80:
  print("Grade: C")
elif mark_percent >=60 and mark_percent<70:
  print("Grade: D")
elif mark_percent >=50 and mark_percent<60:
  print("Grade: E")
else:
  print("Failed")