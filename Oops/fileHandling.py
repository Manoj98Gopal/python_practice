# reading purpose
f = open("file1.txt","r")

# writing purpose
f1 = open("file2.txt","w")


# appending purpose
f2 = open("file1.txt","a")



# print(f.read())      reading enter text in the file

# print(f.readline())   
# print(f.readline())   reading text line by line



# print(f1.write("I am manoj\n"))
# print(f1.write("I am manoj kumar"))     writing the text into the file 


copy = f.read()

print(f2.write(copy))

# arr = f.readlines()

# for i in arr:
# 	print(i)


with open("file1.txt","r") as file:
	for line in file:
		print(line)