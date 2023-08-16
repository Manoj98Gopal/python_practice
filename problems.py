import sys 

print(sys.getrecursionlimit)



# create a fibonacci seriase



print("***************** fibonacci seriese ******************")


fibo = [0,1]

f1 = 0
f2 = 1

for i in range(2,20):
	f3 = f1 + f2
	f1 = f2
	f2 = f3
	fibo.append(f3)

print(fibo)

print("*************** using function ***********************")

def fibonacci(n):
	a = 0
	b = 1

	if n == 1:
		print(a)
		return
	if n == 2:
		print(a)
		print(b)
		return

	print(a)
	print(b)

	for i in range(2,n):

		re = a + b
		a = b
		b = re

		print(re)


# fibonacci(20)


# Factorial of the number 

print("************** factorial of number **********************")

def fact(n):

	r = 1
	
	for i in range(1,n+1):
		r = i * r
		 
	
	print(r)


fact(6)


# Recurtion 
# recurtion means a function call its self is called recurtion

print("***************** with the help of recurtion *******************")

def fac(n):

	if n == 0:
		return 1

	return n * fac(n - 1)



result =  fac(5)

print(result)




v = lambda a : a*a


g = v(5)

print(g)





