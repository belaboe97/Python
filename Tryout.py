mystring = 'hello'
mylist = [x for x in mystring ]
print(mylist)

mylist2 = [x**2 for x in range(0,100) if x%2 == 0]
print(mylist2)


mylist = [ x if x%2 == 0 else '0DD' for x in range(0,100,3)]+
print(mylist)   
calcius = [0,10,20,30,33,55]

fahrenheit = [ ((9/5)*temp +32) for temp in calcius]
print(fahrenheit)

