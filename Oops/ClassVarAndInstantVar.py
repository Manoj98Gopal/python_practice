

# class variable(static variable) and instance variable 

class Car:

	wheels = 4   #class variable 

	def __init__(self):   #intializing
		self.name = "BMW"   #instant variable 
		self.color = "red"


	def update(self,name,color):
		self.name = name
		self.color = color


c1 = Car()   #constractor
c2 = Car()

c2.update("Swift","white")

Car.wheels = 6

print(c1.name,c1.color,c1.wheels)
print(c2.name,c2.color,c2.wheels)


