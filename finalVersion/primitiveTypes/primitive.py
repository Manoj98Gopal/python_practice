# Primitive type

# A primitive is a basic, built in type in python that represent a single, simple value 
# These are the smallest building blocks of any program

# primitive types are 
age = 25           # int
price = 99.99      # float
is_logged_in = True # bool
name = "Manoj"     # str
data = b"ABC"      # bytes
value = None       # NoneType



print("Integer : ",age)
print("Float : ",price)
print("Boolean : ",is_logged_in)
print("String : ",name)
print("Byte : ",data)
print("NoneType : ",value)




# Mutable vs Immutable in Python

# Immutable Types:
# These cannot be changed in place.
# Any change creates a new object with a new memory address.

print("Immutable Example with int:")

a = 10
print("Value of a:", a)
print("Memory address of a:", id(a))

a = a + 5
print("New value of a:", a)
print("New memory address of a:", id(a))
# Memory address is different after change.

print("\n Immutable Example with str:")

name = "Manoj"
print("Value of name:", name)
print("Memory address of name:", id(name))

name = "Ravi"
print("New value of name:", name)
print("New memory address of name:", id(name))
# Again, new memory address after change.


# Mutable Types:
# These can be changed in place.
# Memory address stays the same.

print("\nMutable Example with list:")

numbers = [1, 2, 3]
print("Value of numbers:", numbers)
print("Memory address of numbers:", id(numbers))

numbers[0] = 100
print("Updated value of numbers:", numbers)
print("Memory address of numbers (same):", id(numbers))
# Memory address is same even after changing content.


print("\n Mutable Example with dict:")

person = {"name": "Manoj", "age": 25}
print("Value of person:", person)
print("Memory address of person:", id(person))

person["age"] = 30
print("Updated value of person:", person)
print("Memory address of person (same):", id(person))
# Memory address is same after update.
