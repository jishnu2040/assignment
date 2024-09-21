"""
Write a program to find the grade of a student during his academic year. 
a.	Program should accept the scores for written test, lab exams and assignments
b.	Output the grade of a student (using weighted average)
"""

test = int(input("Enter the Written Exam's Mark: "))
lab = int(input("Enter the Lab Exam's Mark: "))
assign = int(input("Enter the Assignment's Mark: "))

mark = float(test * 0.7 + lab * 0.2 + assign * 0.1)

print("Mark = ", mark)