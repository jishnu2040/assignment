def infinte_counter():
    n = 0
    while True:
        yield n
        n+=1

counter = infinte_counter()


# print(next(counter))
# print(next(counter))

# print(next(counter))
for _ in range(5):
    print(next(counter))