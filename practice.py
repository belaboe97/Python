def old_macdonald(name):
    return name.capitalize()

print(old_macdonald('macdonald'))

def master_yoda(text):
    x =  text.split()
    reversed_string = x[::-1]
    return ' '.join(reversed_string)


print(master_yoda('We are ready'))

def has_33(nums): 
    for i  in nums:
        if nums[i]+nums[i+1]==6:
            return True
        else:
            return False

def has__33(nums):
    string = ""
    for i in nums:
        string += str(i)
    return '33' in string

    
print(has__33([1, 3, 3]))
print(has__33([1, 3, 1, 3]))
print(has__33([3, 1, 3]))

def paper_doll(text):
    newWord = ''
    for x in text.split():
        for y in x:
            newWord += y*3
    return newWord
        

print(paper_doll('heyho mississipii'))

def blackjack(*args):
    blackjack = sum(args)
    if blackjack <= 21:
        return blackjack
    elif 11 in args and blackjack > 21:
        return blackjack-10
    else: 
        return 'BUST'

print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))

def summer_69(num):
    total = 0
    add = True
    for x in num:
        if x != 6 and add:
            total += x
        else:
            if x != 9:
                add =  False
            else: 
                add= True
                
    return total

print(summer_69([1,3,5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))


def spy_game(nums):
    string = ""
    for x in nums:
        string += str(x)
    return '007' in string

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,7,2,0,4,5,0]))


def count_primes(num):
    x = [1,2,3,5,7]
    for prime in range(0,num): 
        if prime%2 == 0 or prime%3 == 0 or prime%5==0 or prime%7==0:
            pass
        else:
            x.append(prime)
    return x

print(count_primes(100)) 

def count_primess(num):
    primes = [ x-x if x%2 == 0 or x%3==0 or x%5==0 or x%7==0 else x for x in range(0,num)]
    return primes

print(count_primess(100))



def factor(x,y):
    return (y%x==0)

def getFactor(x):
    for i in range(1,x+1):
        if factor(i,x):
            print(i)

def isPrime(primeNum):
    totalFactors=0
    for i in range(1, primeNum+1):
        if factor(i,primeNum):
            totalFactors += 1
    if (totalFactors<=2):
        return True
    else:
        raise NotImplementedError
        return False

print(factor(2,4))
getFactor(30)

if isPrime(20):
    print('it is a PrimeNumber')
else:
    print('its not')


print(min(5,8))
print(max(5,6))
