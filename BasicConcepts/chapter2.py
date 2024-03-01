# If Statements:

x = 10


if x > 10:
    print(True)
else:
    print(False)
    
    
# else if statement


if x > 10:
    print("this is first conditon")
elif x == 10:
    print("x is equel to 10")
else:
    print("this is else state")
    
    
    
# For Loops:

fruits = ['apple','mango','banana','grape']

for value in fruits:
    print(value)
    


# using range also we can loop
for x in range(10):
    print(x)
    
    
# While Loops:

x = 0

while x < 5:
    print("print x value =",x)
    x+=1
    
    
# Example Using Control Structures Together:

numbers = [1,2,3,4,5,44,56,7,8,9,6]


for x in numbers:
    if x % 2 == 0:
        print("this value is even ==",x)
    else :
        print("this value is odd ==",x)