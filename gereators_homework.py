import random

#Problem 1
def gensquares(N):
    for i in range(N):
        yield i**2

for numbers in gensquares(10):
    print(numbers)

#Problem 2

def rand_num(low,high,n):
    for randinteger in range(n):
        yield random.randint(low,high)

for randint in rand_num(1,100,10):
    print(randint)

#Problem 3

randint_gen = (item for item in rand_num(5,10,5))
for item in randint_gen:
    print(item)


s = 'hello'
string_iter = iter(s)
print(next(string_iter))
