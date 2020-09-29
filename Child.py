from Human import Human

class Child(Human): 
	def __init__(self,name,height,weight,age):
		Human.__init__(self,name,height,weight)
		self.__age = age

	def get_age(self): 
		return self.__age

	def __str__(self):
		return  f'Is years {self.__age}'

childList = []

Nick = Child("Nick",100,40,9)
Jan = Child("Jan",150,60,13)

childList.append(Nick)
childList.append(Jan)

print(Jan.get_name())


	avgAge = 0

	for age in childList: 
		avgAge += age.get_age()
	avgAge = avgAge/len(childList)




print(Nick.get_age())
print(Jan)
print(avgAge)
