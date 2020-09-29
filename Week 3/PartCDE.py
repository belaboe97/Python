#PART C

# def prime(x):
#    return x%2==0
#
#def allPrime():
#    for i in range(1,101):
#        if prime(i):
#            print(i)
#        else:
#            pass

#PART D
#FACTOR CHECK
def factor(x,y):
    return (y%x==0)
#TEST FACTOR
x=5
y=10
if factor(x,y):
    print(x,"is a factor of",y)

#CHECK PRIME
#PART E
def prime(x):
    totalFactors=0
    for i in range(1, x+1):
        if factor(i,x):
            totalFactors += 1
    return (totalFactors<=2)
 
#TEST PRIME:
#EXPECTED VALUE 1) TRUE 2) FALSE
print(prime(13),prime(20)) 

#PRINT ALL PRIME NUMBERS TO 100
def allPrime():
    for i in range(1,101):
        if prime(i):
            print(i)
        else:
            pass
allPrime()


#OTHER WAYS TO FIND PRIME TILL 100: 
#SIEVE OF ERASTOTHENES

def count_primes(num):
    x = [1,2,3,5,7]
    for prime in range(2,num): 
        if prime%2 == 0 or prime%3 == 0 or prime%5==0 or prime%7==0:
            pass
        else:
            x.append(prime)
    return x

print(count_primes(101))