def hello():

    def greet():
        return '\t its me'

    return greet

greet = hello()


print(greet)
print(greet())

def hey():
    return 'Hi Jose'


def other(some_def_func):
    print(some_def_func())

other(hey)


def new_decorator(orginal_func):

    def wrap_func():
        print('some extra,code')

        orginal_func()

        print('Some extra Code')
    
    return wrap_func 

def func_needs_deco(): 
    print('i want to be decoracted')

new_decorator(func)