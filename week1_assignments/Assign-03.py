"""
    Q_03.   Write a program to find the simple interest. SI=(P*R*n)/100)
"""

p_amt = int(input("Enter the Principal Amount: "))
rate = float(input("Enter the Interest Rate: "))
no_years = float(input("Enter Time Perion (No of Years):"))

simple_interest = (p_amt * rate * no_years)/100

print("Entered \"input\" is ", simple_interest)