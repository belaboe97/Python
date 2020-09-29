
while True:
    try:
        for i in ['a','b','c']:
            print(i**2)
    except TypeError:
        print('The Code sucks!')
        break
    except:
        print('you failed')

    else:
        print('it workd out')
        break

try: 
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    print('You cant divide /0')
finally: 
    print('All Done!')

def ask():
    while True:
        try:
            integer = int(input('Type in a number!'))
        except:
            print('try again')
        else:
            print('perfect!')
            break

ask()



