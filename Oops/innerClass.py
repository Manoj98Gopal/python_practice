
class student:

	def __init__(self,name,marks):
		self.name=name
		self.marks=marks
		self.lap = self.laptop()


	def show(self):
		print("student name =",self.name)
		print("student marks =",self.marks)
		print("lap config =",self.lap.ram,self.lap.cpu,self.lap.hard)


	class laptop:     #inner class

		def __init__(self):
			self.cpu = "i5"
			self.ram = "8gb"
			self.hard = "2tb"







s1 = student("manoj",85)
s2 = student("praveen",45)


s2.show()