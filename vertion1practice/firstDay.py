print("Hello world!")


# declaring variables
name = "Manoj"
age = 26
weight = 70.4
isMarried = False

# accessing variables
print("name : ",name)
print("age : ",age)
print("weight : ",weight)
print("isMarried :",isMarried)

# checking variable type
# if you want to check data type of the variable use  "type" function
print("Name type =",type(name))
print("age type =",type(age))
print("weight type =",type(weight))
print("isMarried type =",type(isMarried))


# type conversion
num_int = 20
num_str = str(num_int)
print("result1",type(num_str))


str_int = "30"
int_str = int(str_int)
print("result2:-",int_str)


# input from user 
FirstName = input("Enter your First name")
SecondName = input("Enter your second name")

fullName = FirstName + " " + SecondName

print("Your full name is :-",fullName)



# string formatting 
print(f"String formate name {fullName}")