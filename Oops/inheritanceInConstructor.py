

class A:

	def __init__(self):
		print(" i am init of A")


	def feature1(self):
		print("I am feature 1")


	def feature2(self):
		print("I am feature 2")		


class B(A):

	def __init__(self):
		print(" i am init of B")
		super().__init__()

	def feature2(self):
		super().feature2()
		print("i am feature 3")


	def feature4(self):
		print("i am feature 4")


a1 = B()

a1.feature2()


