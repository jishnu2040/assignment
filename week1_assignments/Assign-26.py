"""
    26.	Write a list comprehension that returns the list ["1*2=1", "22=4", "32=9", ...., "25*2=625"]
"""

list=["{} x {} = {}".format(i,i,i **2)for i in range(1,26)]

for i in list:
    print(i, end=", ")