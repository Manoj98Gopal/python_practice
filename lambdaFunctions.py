import functions


functions.greet()

# normar function
def greeting ():
	print("hello i am ")


greeting()


# lambda function
great = lambda : print("I am lambda function")

great()


#Addition of two number 

def addition(a,b):
	return a + b

print(addition(5,5))


#lambda function
add = lambda a,b : a + b

print(add(4,3))
		

ls = [3,2,4,6,3,8,2,3,1,8,9,6]

# filtering even using filter method
 
def ev(a):
	return a % 2 == 0

even_num = list(filter(ev,ls))

# using lambda

even = list(filter(lambda a : a % 2 == 0,ls))

print(even_num)
print(even)


# dubling the each numbers using map

sqr = list(map(lambda a : a *a,even))

print(sqr)


# add all numbers using reduce 
from functools import reduce

r = reduce(lambda a,b:a+b,sqr)

print(r)