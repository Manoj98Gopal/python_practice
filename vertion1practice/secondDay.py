# condition statements
# age = int(input("Enter your age : "))
age = 22


if 25 <= age and  32 >= age:
    print("Marriage time")
elif 20 <= age  and 25 > age:
    print("searching job")
elif 13 <= age  and  20 > age:
    print("school time")
else:
    print("Enjoying time")    


test = True

if test and age != 18:
    print("not working not")
else:
    print("working expecting")
    
    
    
# while loop 
count = 1
while count <=5:
    print("while loop test = ",count)
    count = count + 1
        

# for loop
for i in range(10, 15):
    print("for loop test = ",i)
    
    
for i in range(10):
    if i == 4:
        continue
    print("for loop with continue",i)
    
    
for i in range(20):
    if i == 5:
        break
    print("for loop with break = ",i)
    


def greet(data):
    print(f"Good evening {data}")
    
    
def multiply(a,b):
    return a * b

mulResult = multiply(5,10)

print("result ==",mulResult)


def sum_all(*args):
    print(args)
    return sum(args)

total = sum_all(1,2,3,4,5)

print(total)


def printInfo(**kwargs):
    print(kwargs)
    for key,values in kwargs.items():
        print(f"{key}:{values}")
        
printInfo(name="Manoj",age="25")




# practice program 

print("even number 1 to 20")


for i in range(1,21):
    if i % 2 == 0:
        print(i)
        
        
def getAvg(*args):
    return sum(args)/len(args)



avgResult = getAvg(2,3,1,4,5,6,3,45)


def check_even_odd(num):
    if num % 2 == 0 :
        print(f"This {num} is even")    
    else:
        print(f"This {num} is odd")
        
        
check_even_odd(int(input("Enter your number : ")))
        