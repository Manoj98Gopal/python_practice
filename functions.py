
def greet():
	print("i am function model")

greet()


print("@@@@@@@ Adding a two numbers @@@@@@@")

def add(a,b):
	return a + b


result = add(10,20)

print(result)


print("@@@@@ pass value and pass by refrence @@@@@@@@@@@")

# pass by value means, when we calling the function, we are passing the value to that function
# in that function we can update the value , it is not effecting to out side value 

def update (x):
	x = 10
	print("x value=",x)


num = 5
update(num)
print("num value",num)

# pass by referece means, when we calling the function , we are not passing the value , we are passing values refrence
# means we passing the address of the varialbe , when we change the address of the value it is effect on original value too.

def updlst(lst):
	lst = [1,2,3]
	print(lst)

lst = [2,3,3]
updlst(lst)

print(lst)

# in the python we are not using any of this concept 



