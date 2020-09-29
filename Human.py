class Human: 

	def __init__(self,name,height,weight):
		self.__name=name
		self.__height =height
		self.__weight =weight

	#Getter && Setter

	def set_name(self,name):
		self.__name =name 

	def get_name(self):
		return self.__name



Otto = Human("otto",185,90)

print(Otto.get_name())