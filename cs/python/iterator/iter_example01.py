from re import S

s =  'abc'

for char in s:
    print(char)

s = 'abc'
it = iter(s)
while True:
    try:
        print(next(it))
    except StopIteration:
        del it
        break



