
# variables

age = 25            #integer
name = "Manoj G"    #string
is_Coder = True     #boolean


#Data types

age = 44                               #Integer       :-  Represents whole numbers without any decimal points.
height = 6.1                           #Float value   :-  Represents numbers with decimal points.
name = "Manoj Achar"                   #String        :-  Represents text data, enclosed within single or double quotes.
is_Dancer = False                      #Boolean       :-  Represents truth values, True or False.
numbers = [1,2,3,4,5,6]                #list          :-  Represents an ordered collection of elements. Elements can be of different data types.
cordinates = (3,5)                     #tuple         :-  similar to lists, but immutable (cannot be modified after creation).
person = {'name':'Manoj','age':'25'}   #dictionary    :-  Represents a collection of key-value pairs.
unique_number = {1,2,3,4,5}            #Set           :-  Represents an unordered collection of unique elements.




# ------------------------- List manipulation -----------------------------------------

# creating list 
my_list = [1,2,3,4,5,6]

# append() method adds a single element to the end of the list.
my_list.append(10)

# extend() method appends elements from another iterable to the end of the list.
my_list.extend([11,12,13,14])

# insert() method inserts an element at a specified index in the list.
my_list.insert(0,55)

# remove()  remove specific element
my_list.remove(12)

# pop()  based on index number it is removing if index is not specified it is removed last elemtn
removedElement1 = my_list.pop(1)
removedElement2 = my_list.pop()

# print("removed based on index ==",removedElement1)
# print("removed last element ==",removedElement2)


#Indexing and slicing
access_specific_index = my_list[2]
access_slice_part = my_list[2:7]


# reversing the list 
temp_list = [1,2,3,4,5,6]
temp_list.reverse()

#sorting the element 
unsorted_list = [4,3,5,6,4,2,1,2,3]
unsorted_list.sort()


# we can clear the list 
temp_list.clear()



# ------------------------- dictionary manipulation -----------------------------------------


#Dictionaries creation
my_dict = {
    "name" : "Manoj G",
    "age" : 25
}


#we can acess the data in two way
# 1)first way
one = my_dict["name"]

# 2)second way
second = my_dict.get("age")



# Iterating Over Items

#using loop
for key, value in my_dict.items():
    print("keys ===",key, "values ===",value)
    
    

#we can update dictionary in two ways

# 1) using square brackets
my_dict["city"] = "Mysore"
my_dict["age"] = 26

# 2) using update method
my_dict.update({"name" : "Manoj Achar","degree" : "BCA"})



# Checking for Key Existence:

# Using 'in' keyword
if 'age' in my_dict:
    print("age is exisiste")
else:
    print("age is not existit")


#using key method
if 'name' in my_dict.keys():
    print("keys method exist")



# Getting Keys and Values:

my_dict_keys = my_dict.keys()
my_dict_values = my_dict.values()


print("my dict keys ==",my_dict_keys)
print("my dict values ==",my_dict_values)


#Removing Element from dictionary

# 1) using pop() method
my_dict.pop("degree")

# 2) using del keyword
del my_dict['city']
    
    
    
# Clearing dictionary

my_dict.clear()

print(my_dict)

