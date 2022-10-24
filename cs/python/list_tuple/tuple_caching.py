from timeit import timeit

print(timeit("[1,2,3,4,5,6,7,8,9]", number=10000000))
print(timeit("(1,2,3,4,5,6,7,8,9)", number=10000000))
