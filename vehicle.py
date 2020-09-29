class vehicle: 

    #CONSTRUCTOR
    def __init__(self,regNum,make,model,milesOnClock):
        self.__regNum = regNum
        self.__make = make
        self.__model = model
        self.__milesOnClock = milesOnClock
    
    #SETTER && GETTER
    def set_miles(milesOnClock):
        self.__milesOnClock = milesOnClock
    
    def get_make_model(self):
        return self.__make
    
    def get_miles(self):
        return self.__milesOnClock
    
    def __str__(self):
        return f'{self.__model}'

car = vehicle(10101,'BMW','i4','300') 


print(car,car.get_miles() )

