# polymarphims means  poly means single and marphims  means  forms
# we can achive through  DUCK TYPE, OPERATOR OVERLOADING, METHOD OVERLOADING


# Duck type

class Dog:

	def sound(self):
		return "Bow Bow...."


class Cat:

	def sound(self):
		return "Meom Meom...."


class Duck:

	def sound(self):
		return "byak byak..."


def make_sound(animal):
	print(animal.sound())


# method name is same but diffrent behaviour

dog = Dog()
cat = Cat()
duck = Duck()

make_sound(duck)



# method overloading 

# method overloading means a class have more than one method with same name but diffrent parmiters is called method overloadig 
# but in python we cant achive the methodoverloading , because we arent able to create same name of method in same class 
# we are achive same concept in diffrent approch


class Calc:

	def add(self,a=None,b=None,c=None):

		r = 0

		if a != None and b != None and c != None:

			r = a + b + c

		elif a != None and b != None:

			r = a + b

		else:

			r = a


		return r

		


c1 = Calc()

print(c1.add(3))


# method overriding

# method overriding concept come into picture , when we use inheritance ,  overriding means it overrides the method 

class A:

	def call(self):
		print("i am A")


class B(A):

	def call(self):
		print("this is overriding method ")



b1 = B()


b1.call()
