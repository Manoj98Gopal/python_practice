
# list data type 

# creating list 
print("------------------ creating list ---------------------")
a = []
b = [1,2,3,4,5,6]
c = [True,False,1,34.1,"Ram"]
d = list("Hello")

print(a)
print(b)
print(c)
print(d)


# accessing list
print("------------------- accessing list --------------------")
lst = [10,30,1,34,42,64,33,28,1,34]

print("accessing last index",lst[-1])
print("accessing first index",lst[0])
print("accessing slice method",lst[1:5])
print("checking length of list",len(lst))


# modifying elements
lst[1] = 100
print("modifying element of 1st index",lst)


# appending elements after appending value will insert to last
lst.append(555)
print("appended result ==",lst)


# insert method using this we can insert specific index  it accept first param as  index second as  value
lst.insert(1,333)
print("insert result =",lst)

# extend method using this we extend the  array list 
tempList = [99,88,77,66]
lst.extend(tempList)
print("after extended result ==",lst)


# removing elements from list
tempList.remove(88)
print("after remove method temp list =",tempList)

# using pop we can remove based on index value
tempList.pop(0)
print("after pop method =",tempList)

# using clear method we can empty the array
tempList.clear()
print("after clear the method",tempList)

# using index method we can search element which place is it occurring 
print("search 34 value where is occurred : ",lst.index(34))

# using count method we can get result how many times that number is occurring in the list
print("how many times 34 is occurring in list :",lst.count(34))


# sorting and reversing the list 
lst.sort()
print("sort the list using sort method : ",lst)
lst.reverse()
print("reverse the sort list ==",lst)


# copying list 
original = [1,2,3,4,5]
copy1 = original.copy()
copy2 = list(original)
copy3 = original[:]

print("copy using copy method :",copy1)
print("copy using list method :",copy2)
print("copy using using slice :",copy3)


print("checking condition value is there in list ",11 in original)

# iteration using for loop
for i in original:
    print(i)
    
# iteration accessing index and value
for idx, val in enumerate(original):
    print(f"index {idx} : value {val}")
    
    
    
users = [
    {"id": 1, "name": "Alice", "age": 25},
    {"id": 2, "name": "Bob", "age": 30},
    {"id": 3, "name": "Charlie", "age": 28}
]

for i in users:
    print(i)