
#  We have three types of error , 1) syntax error, 2) compiled error, 3) runtime error 
#  syntax error means , while we coding we write wrong syntax , for example wrong spelling or indentation propblem
#  compiled error means, while we writing code , after compiled we can see those error, for example 3 + 1  = 5 this is currect result , if got 4 that is compiled error 
#  runtime error means, while we coding  some many cases we need to take input from user, in that case we facing runtime error  means it is not compiled complitly



a = 5
b = "j"


try:
	result = a / b
	print(result)

except Exception as e:
	print("your trying to divide by 0",e)

try:
	print("database connection open")
	result = a / b

except Exception as e:
	print(e)

finally:
	print("database conncetion close")