def fibanoci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibanoci(n-1) + fibanoci(n -2)
    

res = fibanoci(10)
print(res)