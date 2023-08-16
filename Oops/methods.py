
# instance method
# class method
# static method
# getters ()



class Human:

	class_variable = "I am class variable"

	def __init__(self):

		self.eyes = 2
		self.legs = 4

	# instance method
	def get(self):

		print(self.eyes)
		print(self.legs)

	# instance method	
	def setter(self,value):

		self.legs = value

	
	# class method
	@classmethod  #decoraitors
	def call(cls):
		print("i am class method =",cls.class_variable)

	# static method 
	@staticmethod
	def greeting():

		print("i am static methods")




Teacher = Human()

Teacher.get()

Teacher.setter(55)

Teacher.get()

Human.greeting()

Human.call()


