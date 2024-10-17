# stack implementation using list

lst = []

lst.append(10)
lst.append(49)
lst.append(100)

print(lst)
lst.pop()

print(lst)

if len(lst) == 0:
    print("stack is empty")

print(lst[-1])