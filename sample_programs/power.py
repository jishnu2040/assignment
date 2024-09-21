num = int(input("enter a number"))
i=1
temp = num
flag =1
while temp >= 1:
    i=i*2
    if num == i or num == 1:
        flag = 1

num = num/2
if flag == 1:
    print("number is power of 2")
else:
    print("number is not power of 2")
    