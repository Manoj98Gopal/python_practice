i = 0


print("+++++++++++++++++++ While Loop ++++++++++++++++++")

while i < 5:
	print("Hello ",end="")
	i += 1
	j = 0
	while j < 4:
		print("Manoj ",end="")
		j += 1
	print()


print("+++++++++++++++++++ for Loop ++++++++++++++++++")


names = ["manoj","Manoj achar","Manoj Gopal","manu","manu Man"]

for i in names:
	print(i)




print("++++++ Using range printing revers order +++++++++++++")

for i in range(10 , 0,-1):
	print( " ",i,end="")
print()	




print("++++++ Using range printing 11 to 20 +++++++++++++")

for i in range(11 , 21,1):
	print( " ",i,end="")
print()	

print("++++++ how to exit the  loop with the help of 'BREAK' +++++++++++++")


for i in range(0,20,1):
	if i == 12:
		break
	print(" ",i,end="")
print()

print("++++++ how to skip the iteration with the help of 'CONTINUE' +++++++++++++")


for i in range(20):
	if i == 3:
		continue
	print(" ",i,end="")

