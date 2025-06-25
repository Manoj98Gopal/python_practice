print("********************* While loop *******************************")

num = 1

while num <= 5:
    print(num * "*")
    num += 1
    


print("********************* forloop *********************************")

prices = [10,20,30,40]
total = 0

for p in prices:
    total += p
    
print(f"Total is {total}")


print("*****************************  Nested Loop ******************************")

for x in range(4):
    for y in range(3):
        print(f"({x},{y})")
        
        
print("print f latter in stars ")

f_letter = [5,5,2,2,5,5,2,2,2]

for x in f_letter:
    print("#" * x)
    
    
print("l letter in #")

l_letter = [3,3,3,3,8,8]

for x in l_letter:
    print("#" * x)