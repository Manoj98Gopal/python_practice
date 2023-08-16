from array import*


v = array("i",[2,3,4,5])

print("========== Finding the length of array =================")

arrayLength = len(v)

print(arrayLength)


print("========== adding elements to the array using append,insert,extend ================")


v.append(32)
v.insert(0,23)
v.extend([44,55])

print(v)

print("========== removing elements to the array ================")

v.pop(1)
v.remove(55)

print(v)

num = array("i",[2,3,4,3,5,6,8,7])

print("============== Looping elements to the array ===================")


for i in num:
	print(i)


print("+++++++++++++++ Searching a element in an arrya +++++++++++++++++")

numbers = array("i",[23,44,2,6,4,7,8,9,1,])

val = 9;

index = 0
for i in numbers:
	if i == val:
		print(f"element index number is {index}")
	index +=1;


print("+++++++++++++++ Searching a element in an arrya with the help method+++++++++++++++++")

print(numbers.index(val))