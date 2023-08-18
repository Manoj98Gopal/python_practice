
idx = -1

def search(list,n):

	i = 0

	while i < len(list):



		if list[i] == n:
			globals()["idx"] = i

			return True

		i +=1	


	return False




list = [2,3,4,5,7,9,76,23]

n = 3






def search1(list,n):



	for i in list:


		globals()["idx"] += 1

		if i == n:

			return True

	return False



if search1(list,n):

	print("found at =",idx)
else:
	print("not found")




print("++++++++++++++++++++++++ Binary search +++++++++++++++++++++++++++")

pos = 0

def binary(list,n):

	l = 0
	u = len(list) - 1


	while l <= u:

		mid = (l + u) // 2

		if list[mid] == n :

			globals()["pos"] = mid

			return True

		if list[mid] < n :

			l = mid + 1

		else :

			u = mid - 1

	return False
	





ls = [1,2,23,45,78,90,345,434,]		


find = 45


if binary(ls,find):

	print("found at =",pos)

else:

	print("Not found")









