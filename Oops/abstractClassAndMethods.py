
# abstract method means  , a method doesn't have body is called abstract method and  a class have abstract method is called abstract class
# An abstract method is a method declared in a base class (abstract class) but without any implementation. 
# It's meant to be overridden by the subclasses. An abstract class is a class that cannot be instantiated
# directly and is meant to be subclassed to provide concrete implementations for its abstract methods.

from abc import ABC, abstractmethod


class student:

	@abstractmethod
	def greet(self):
		pass

class std(student):

	def greet(self):
		print("i am printing")


s = std()

s.greet()



