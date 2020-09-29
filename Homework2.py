import math 

def vol(rad):
   return  2 * math.pi * rad

print(vol(2))

#2 
def ran_check(num,low,high):
    if low < num < high: 
        return ('The {} number is between {} and {}'.format(num,low,high) )
    else: 
        return ('OUT OF BOUNCE')

def ran_check_true(num,low,high):
    return low < num < high

def ran_check_range(num,low,high):
    return num in range(low,high) 
    


print(ran_check(5,2,7),ran_check_true(5,2,7),ran_check_range(5,2,7))
string = 'Hello Mr. Rogers, how are you this fine Tuesday?'

def up_low(string):
    countUp = 0
    countLow = 0
    for i in string:
        if i.isupper():
            countUp += 1 
        else: 
            countLow += 1
    return countUp,countLow

print(up_low(string))

mylist= [1,1,1,1,1,2,2,3,4,5,5,5,5]
def unique_list(mylist):
    return set(mylist)

print(unique_list(mylist))

def unique_list1(mylist):
    setlist = []
    for x in mylist: 
        if x in setlist:
            pass
        else:
            setlist.append(x)
    return setlist

print(unique_list1(mylist))

numberlist = [1,2,3,-4]
numberlist1 = [2,3,4]
def multiply(numbers):
    product =  1
    for num in numbers:
        product *= num
    return product

print(multiply(numberlist))
print(multiply(numberlist1))

def palindrome(s):
    return s == s[::-1]

print(palindrome('helleh'))

import string

def ispangram(str1):
        string = ''
        counter = 0
        alpha = False
        for i in str1.lower().strip():
            if i in string: 
                if i == 26: 
                    alpha = True
                    break
                else:
                    pass
            else: 
                string += (i)
                counter += 1 
        return alpha,counter,string

print(ispangram("The quick brown fox jumps over the lazy dog"))
