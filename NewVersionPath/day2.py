import math

# Arithmetic operators 
x = 10
y = 3 

print("*************** Arithmetic operation ********************")

print(x + y) # addition
print(x - y) # subtract
print(x * y) # multiplication
print(x / y) # division
# another methods of  division
print(x // y) # division  result without decimal
print(x % y)  # modules 
print(x ** y) # square



print(math.ceil(5.3333))
print(math.floor(5.3455))



print("***************** if statement *********************************")

is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print("drink plenty of water")
elif is_cold:
    print("It's is cold day")
    print("Ware warm cloths")
else:
    print("It's Lovely days")
    
    

print("************************** practice if statements **********************")

price_of_house = 100000
is_user_as_good_credit = False
down_payment = 0

if is_user_as_good_credit:
    down_payment = price_of_house * 0.1
else:
    down_payment = price_of_house * 0.2
    
print(f"down payment is ${math.ceil(down_payment)}")



print("****************************** logical operator ****************************")


has_good_credit = True
has_high_income = False
has_criminal_record = False

# and 
# or
# not

if has_good_credit and not has_criminal_record:
    print("User is eligible of Loan")
else : 
    print("User is not eligible of Loan")




print("******************************* comparison operator *****************************")

temperature = input("what is the temperature now ?")
 
if int(temperature) > 30 :
    print("It's hot day")
elif int(temperature) < 10 :
    print("It's cold day")
else:
    print("It's neither hot or cold")
     