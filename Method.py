
def secret(word):
    first_letter = word[0]
    if first_letter in 'aeiou':
        pig_word =  word+'ay'
    else:
        pig_word =  word[:1] + first_letter + 'ay'
    return pig_word

print(secret('word'), secret('apple'))

def myfunc(*args):
    mylist= []
    for x in args:
        print(x)
        if x%2==0:
            mylist.append(x)
            return  mylist

print(myfunc(1,3,5,7,8,3))


def myfunc1(string):

    count = len(string)
    newString = ""
    for i in range(count):
        if i%2 == 0:
            newString += string[i].upper()
        else:
            newString += string[i].lower()
    print(count)
    return newString
            
            
