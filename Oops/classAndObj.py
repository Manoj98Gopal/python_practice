# oops means object oriented programming language
# object is a instance of a class, object has a diffrence argumenst and methods 
# class is a blueprint of a object 


class Computer:

	def __init__(self,cpu,ram):

		self.cpu = cpu
		self.ram = ram

	def config(self):
		print("config is ",self.cpu,self.ram)





comp1 = Computer("i5","16gb")  #constractor
comp2 = Computer("reyzan 3","8gb")


comp1.config()
comp2.config()