

# Lambda function 


# normal function 
def squre(value):
    return value * value


# lambda function
result = lambda x : x*x


print(squre(4))
print("lambda result : ",result(5))


# higher order function it is taking the function as a argument
def special(fun,a,b):
    fun(a,b)

def add(a,b):
    print ("Addition = ",a+b)
    
def sub(a,b):
    print ("Substraction =",a-b)
    
    
special(add,20,30)    
