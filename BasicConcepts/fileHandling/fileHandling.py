

#writing the file from code 
f = open('example.txt','w')

con = "this is new line from code "

f.write(con)

f.close()


# appending the new content to file 
file = open('example.txt','a')
content = "\nAppending new content"

file.write(content)

file.close


# read the data from the file 
file = open('example.txt','r')

content = file.read()

print(content)

file.close()



file = open('data.txt','w')

file.write(content)

file.close()
