class Line:
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2 
    
    def slope(self):
        pass

    def distance(self):
        #x = self.coor1[0]-self.coor2[0]
        #y = self.coor2[1]-self.coor2[1]
        #return ((x**2)+(y**2))**0.5
        return ((((self.coor2[0]-self.coor1[0])**2)+((self.coor2[1]-self.coor1[1])**2))**0.5)

    def slope(self):
        return (self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0])



    def __str__(self):
        return f'The distance between A and B is: {self.distance()} and the slope is{self.slope()}'


line1 =  Line((3,4),(5,6))
li = Line((3,2),(8,10))
print(li.distance())
print(line1.coor1[0])
print(line1.distance())
print(li)

class Cylinder:

    pi = 3.14
        
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius


    def volume(self):
        return self.pi*self.radius**2*self.height

    def surface_area(self):
        return 2*self.pi*self.radius**2

    def __str__(self):
      return  f'The Volume is {self.volume()} and the surface_area is {self.surface_area()}'

c = Cylinder(2,3)

print(c)

class Account: 
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def deposit(self,money):
        self.balance += money
        return 'Deposit accepted'

    def withdraw(self,moneytaken):
        if self.balance < moneytaken:
            return 'Funds Unavailable'   
        else:
            self.balance -= moneytaken
            return 'Withdraw Accepted'

    def __str__(self):
        return f'Account owner: {self.name}\nAccount balance: {self.balance}$'
    
   

   

acct1 = Account('jose',100)



print(acct1)
print(acct1.withdraw(1000))
print(acct1.balance)
print(acct1.deposit(101))
print(acct1.balance)
