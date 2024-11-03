def squares(length):
    for n in range(length):
        yield n ** 2


s = squares()
print(s)