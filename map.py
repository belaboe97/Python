def square(num):
    return num**2

my_nums = [1,2,3,4,5,6]
for item in map(square,my_nums):
    print(item)

print(list(map(square,my_nums)))

def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else: 
        return mystring[0]

names = ['Andy', 'EVE , Sally','PUPy']

print(list(map(splicer,names)))

mynums= [1,2,3,4,5,6]

def check_even(num):
    return num%2 == 0

print(list(filter(check_even,mynums)))

def square(num):
    return num**2

print(list(map(lambda num : num**2,mynums)))

print(square(3))