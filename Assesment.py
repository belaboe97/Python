
#Number1
st = 'Print only the words that start with s in this sentence'

for x in st.split(): 
    if x[0]=='s':
        print(x)
    else: 
        pass
#Number2
evenNumbers = [ even for even in range(0,11) if even%2==0]
print(evenNumbers)

#Number3
list1 =  [ num for num in range(3,50,3)]
list2 = [num for num in range(1,50) if num%3==0]
print('{}\n{}'.format(list1,list2))

#Number4
st = 'Print every word in this sentence that has an even number of letters'
evencounter = 0
for x in st.split():
    if len(x)%2==0:
        print('EVEN')
        evencounter += 1
    else:
        print('ODD')
print('Evenwords:',evencounter)

#Number4
i = 0
while i<100: 
    i = i + 1
    if i%3==0:
        if  i%5==0:
            print('FizzBuzz')
        else: 
            print('Fizz')
        continue
    if i%5==0:
        print('Buzz')
        continue
    if i%3==0 and i%5==0:
        print('FizzBuzz')
        continue
    else:
        print(i)


st = 'Create a list of the first letters of every word in this string'

listtry = [x[0] for x in st.split()]
print(listtry)


