
print("++++++++++++++ Squre +++++++++++++++++")

for i in range(3):
	print(" ","#",end="")
	for j in range(3):
		print(" ","#",end="")
	print()


print("++++++++++++++ Triagle +++++++++++++++++")

for i in range(4):
	print(" ","*",end="")
	for j in range(i):
		print(" ","*",end="")
	print()


print("++++++++++++++ Rivers Triagle +++++++++++++++++")

for i in range(4):
	print(" ","*",end="")
	for j in range(3 - i):
		print(" ","*",end="")
	print()
