
print("++++++++++++++ Buble sort ++++++++++++++++++")


def  buble(list):

	for i in range(len(list)):

		for j in range(len(list)):

			# print(i,j)

			if list[i] < list[j]:

				temp = list[i]
				list[i] = list[j]
				list[j] = temp

	return list



print("++++++++++++++ Selection sort +++++++++++++++++++")

	
def selection(list):


	for i in range(len(list)):

		min = i

		for j in range(i+1,len(list)):

			if list[i] < list[j]:

				min = j

		temp = list[i]
		list[i] = list[j]
		list[j] = temp

	return list

			











ls = [8,3,5,2,9,1]

print(buble(ls))	

print(selection(ls))