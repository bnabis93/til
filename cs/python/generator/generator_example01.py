def gen_123():
    yield 1
    yield 2
    return 4 # StopIterator
    yield 3


print(gen_123())

for i in gen_123():
    print(i)


g = gen_123()
print(next(g))
