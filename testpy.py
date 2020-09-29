class Animal:

	def __init__(self,name, food):
		self.name = name
		self.food = food 

	def get_name(self):
		return self.name

	def set_name(name):
		self.name = name



class Dog(Animal):

	def __init__(self, name, food,race):
		Animal.__init__(self,name,food)
		self.race = race

	def get_race(self):
		return self.race

	def set_race(self, race): 
		self.race = race


Hund = Dog("Wuff", "Pizza", "Labrador")

print(Hund.get_race())
Hund.set_race("Pudel")
print(Hund.get_name())