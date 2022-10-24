from timeit import timeit

print(timeit("range(10)", number=10000000))
print(timeit("range(100)", number=10000000))
print(timeit("range(1000)", number=10000000))
print(timeit("range(10000)", number=10000000))
print(timeit("range(100000)", number=10000000))
