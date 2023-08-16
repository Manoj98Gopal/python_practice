
# Data types 

#	1)None
#	2)Numeric
#		a) integer
# 		b) float
#   	c) complex
#		d) bool
# 	3) Sequence
#		a) list
#		b) tuple
# 		c) set
# 		d) string
#		e) range
#	4) Dictionary


# integer 
num1 = 456

# float
num2 = 45.2

# bool
num3 = True

#complex
num4 = 4+5j

print(type(num1))
print(type(num2))
print(type(num3))
print(type(num4))

# type convertions 

num1 = float(num1)
num2 = int(num2)


print(num1)
print(num2)

print(type(num1))
print(type(num2))


#list
num5 = [34,5,23,45,76,8]

#tuple
num6 = (23,34,23,67,43)

#set
num7 = {56,45,97,34,64}

#string
num8 = "Manoj Kumar"

#range
num9 = range(10)

print("----------------------")
print(type(num5))
print(type(num6))
print(type(num7))
print(type(num8))
print(type(num9))


print("-------------")

num10 = {
	"manu" : "javascript",
	"ram" : "Python",
	"vivek" : "PHP"
}

print(type(num10))

print(num10.get("ram"))



