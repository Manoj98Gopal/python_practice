import utils
from utils import find_large_num
from utils import find_small_num

import ecommerce.shipping
from ecommerce.shipping import calculate,greet



print("************************** functions *******************************")

def greeting(name):
    return f"Good morning {name}"



print(greeting("Manoj"))



print("********************************** with arguments **************************")

def get_total(total,gst = 10):
    try:
        return total + gst
    except Exception as e :
        print("Something went wrong",e)
    finally:
        print("Finally Done")


print(get_total(total=2345,gst="dasdads"))



print("********************************  class ************************************")



class Point:
    
    def draw(self):
        print("draw...")
    
    def move(self):
        print("move...")
        
        

point1 = Point()

point1.draw()
point1.move()
point1.x = 10
point1.y = 20

print(point1.x)

point2 = Point()

point2.draw()
point2.move()


print("***********************************constructor***************************")


class Person:
    
    # constructor when object is creating this function will run
    def __init__(self,name):
            self.name = name
            
    def talk(self):
        print(f"{self.name} is talking...")
        
        
person1 = Person("Manoj G")

person1.talk()

person2 = Person("RamKumar")

person2.name = "Prem Kumar"

person2.talk()



print("*********************** inheritance ****************************")

class Mammals:
    
    def walk(self):
        print("Walking..")
        
        
class Cat(Mammals):
    pass
        
class Dog(Mammals):
    pass
        
        
cat1 = Cat()

cat1.walk()

dog1 = Dog()

dog1.walk()




array = [33,22,4,3,222,5,46,55,20,3]


result1 = find_large_num(array)
result2 = find_small_num(array)

print("large num : ",result1)
print("small num : ",result2)



calculate()
ecommerce.shipping.greet()