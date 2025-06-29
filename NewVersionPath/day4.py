print("************************* List ********************************")

names = ["Manoj","Kumar","Pavan","Mahesh","Ram"]


# accessing the element
print(names[1])
# accessing first element
print(names[0])
# accessing last element
print(names[-1])

print(names[1:3])
print(names)


# updating element inside the list 
names[0] = "Manoj Gopal"

print("updated list : ",names)


print("**************** 2d array ****************************")


two_d_array = [
    [1,2,3],
    [3,5,4],
    [8,5,9]
]

print(two_d_array[0][1])



print("******************** list methods ***********************")


numbers = [2,3,4,1,7,4,9]

# adding number into to the array
numbers.append(100)

# adding element into to list in exact index
numbers.insert(1,200)

# remove element from an array
numbers.remove(2)

# remove last element of an array
numbers.pop()

# find index of the number
index_of_nine = numbers.index(9)

# copy of the list
number2 = numbers.copy()

# sort an element 
numbers.sort()

# reverse an array list
numbers.reverse()

# find how many time  a specific number is occurred in a list
no_of_time = numbers.count(4)


# check number is there or not in the list 
result = 30 in numbers
print("Is 30 in the list?:", result)


print("number of times = ",no_of_time)

print("copy list : ",number2)
print("new list : ", numbers)


# clear the list 
number2.clear()

print("cleared list : ", number2)



print("***************************** tuples **********************************")

data = (1,2,3)


print("tuples : ",data[0])

# unpacking a data 

(a,b,c) = data

print(a+b+c)


print("***************************** dictionary *****************************")


customer = {
    "first_name" : "Manoj",
    "last_name" : "Gopal",
    "age" : 26,
    "is_verified" : True
}

print("created dictionary : ",customer)

# ADD 
customer["email"] = "manoj98Achar@gmail.com"


print("After adding email : ",customer)


# UPDATE
customer["age"] = 25
customer.update({"first_name" : "Manu", "last_name" : "Man"})


print("After updating : ",customer)

# READ
print("Accessing specific key :",customer["first_name"])
print("Accessing specific key with safe method :", customer.get("last_name","LAST NAME MISSING"))
print("Accessing all keys :",customer.keys())
print("Accessing all values :",customer.values())
print("Accessing all key values :",customer.items())


# DELETE
del customer["email"]
print("After deleting email key : ",customer)

customer.pop("last_name")
print("After deleting last_name Key : ",customer)

customer.popitem()
print("After delete last key :",customer)

customer.clear()
print("After delete all keys :",customer)