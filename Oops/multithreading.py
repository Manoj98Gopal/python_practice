#  multithreading means multiple task happend simultaniously

from threading import *
from time import *


class Hello(Thread):

	def run(self):

		for i in range(5):
			print("Hello")
			sleep(1)

class Hi(Thread):

	def run(self):

		for i in range(5):
			print("Hi")
			sleep(1)


s1 = Hello()
s2 = Hi()

s1.start()
s2.start()

s1.join()
s2.join()

print("both are completed")





def a():
	for i in range(5):
		print("I am A-----")
		sleep(1)


def b():
	for i in range(5):
		print("I am B******")
		sleep(1)


thread1 = Thread(target=a)
thread2 = Thread(target=b)


thread1.start()
thread2.start()

thread1.join()
thread2.join()

print ("all threads are completed")