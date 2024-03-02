
# Single level inheritance
class Animal:
    
    def make_sound(self):
        print("Animal is making sound ")
        
        
        
class Cat(Animal):
    
    def type_Of_sound(self):
        print("Meom meom meoum....!")
        
        
cat1 = Cat()
 
cat1.make_sound()
cat1.type_Of_sound()


print("-------------------single level inheritance end ------------------")


# multi level inheritance
class ChildCat(Cat):
    
    def eat(self):
        print("child cat is eating bread..!")
        
        
childCat1 = ChildCat()

childCat1.type_Of_sound()
childCat1.make_sound()
childCat1.eat()



print("-------------------multi level inheritance end ------------------")


# multiple inheritance
class A():
    
    def callB(self):
        print("calling a class")    
        

class B():
    
    def callb(self):
        print("class b is calling")
        
        
class C(A,B):
     
    def callc(self):
        print("calling the class c")
        
        
c1 = C()

c1.callc()
c1.callB()
c1.callb()