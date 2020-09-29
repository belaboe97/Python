def isEven(x):
    return x%2==0

def allEven():
    for i in range(1,101):
        if isEven(i):
            print(i)
        else:
            pass
allEven()