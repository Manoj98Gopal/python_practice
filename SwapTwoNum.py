
a = 10
b = 15


# use third variable 

temp = a;
a = b;
b = temp


print(a,b)


# without using third variable

print("-------------with out using 3rd variable----------------")

a = 4 
b = 8

a = a + b
b = a - b
a = a - b

print(a,b)

print ("-------------------shortest way to swap -----------")

a = 49
b = 22

a,b = b,a

print(a,b)




