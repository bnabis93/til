import itertools

gen = itertools.count(1, 0.5)
for val in gen:
    print(val)

    if int(val) == 5:
        break

gen = itertools.takewhile(lambda n: n < 3, itertools.count(1, 0.5))
print(list(gen))
