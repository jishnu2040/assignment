def sumOfNum(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sumOfNum(n //10)
    
res = sumOfNum(1234466)
print(res)