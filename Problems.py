print("########### Prime Number ##############")

num = 13

for i in range(2,num):
	if  num % i == 0:
		print("not prime")
		break
else:
	print("prime number")


for i in range(2,20):
	for j in range(i):
		if j > 1 :
			if i % j == 0:
				print(i)