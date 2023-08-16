from numpy import *


val = array([2,3,4,5,6,7,])

print ("************* how to copy an array we have three types ******************")

arr1 = array([1,2,3,4,5,6])

print("******* first method assignment operator , in this method  array variable address is same ************ ")

arr2 = arr1

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))


print("********** second method using view method , in this metod array variable address is diffrent but it is shalow copy********")
print("***** shalow copy means after assigment of second variable if try to change firt one it will change both arrays ****")

arr3 = arr1.view()

arr1[1] = 55

print(arr1)
print(arr3)

print(id(arr1))
print(id(arr3))

print("********* third method using copy method , in this method array variable address is diffrent but it is deep copy **********")
print("******** deep copy means if try to change first array after assigment of second one it wont change 2nd array")

arr4 = arr1.copy()

arr1[0] = 88

print(arr1)
print(arr4)

print(id(arr1))
print(id(arr4))
