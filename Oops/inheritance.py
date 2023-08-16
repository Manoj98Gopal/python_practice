

#single level inheritance

print("++++++++ single level +++++++++++")

class A:


	def feature1(self):
		print("I am feature 1")


	def feature2(self):
		print("I am feature 2")		


class B(A):

	def feature3(self):
		print("i am feature 3")


	def feature4(self):
		print("i am feature 4")


a1 = B()
a1.feature2()



#muilti level inheritance

print("++++++++ multi level +++++++++++")


class A1:

	def feature1(self):
		print("featre 1 is working...")


	def feature2(self):
		print("featre 2 is working...")



class B1(A1):

	def feature3(self):
		print("featre 3 is working...")


	def feature4(self):
		print("featre 4 is working...")


class B1(A1):

	def feature3(self):
		print("featre 3 is working...")


	def feature4(self):
		print("featre 4 is working...")


class C(B1):

	def feature5(self):
		print("featre 5 is working...")


	def feature6(self):
		print("featre 6 is working...")		



c1 = C()

c1.feature1()
c1.feature3()



# multiple inheritance

print("++++++++ multiple level +++++++++++")


class A2:

	def feature1(self):
		print("featre 1 is working...")


	def feature2(self):
		print("featre 2 is working...")



class B2():

	def feature3(self):
		print("featre 3 is working...")


	def feature4(self):
		print("featre 4 is working...")

class C2(B2,A2):

	def feature5(self):
		print("featre 5 is working...")


	def feature6(self):
		print("featre 6 is working...")		



rr = C2()


rr.feature3()
rr.feature1()