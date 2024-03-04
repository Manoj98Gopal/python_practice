# inheritance is mechanism of accessing the parent class properties and behaviours ( methods and variables )



# Single level inheritance

class Car:
    
    def __init__(self,model,prize):
        self.model = model
        self.prize = prize
        
    def getWash(self):
        print(f"your car model number is this  {self.model}, whasing completed...!")
        
        
        
class Four_seat(Car):
    
    def __init__(self,model,prize,color):
        # calling parent class constructor
        super().__init__(model,prize)
        self.color = color
        
    def getDetails(self):
        print("Car Model : ",self.model)
        print("Car Color : ",self.color)
        print("Car prize : ",self.prize)
        
        
        
        
maruthi = Four_seat(2018,800000,"Red")

maruthi.getDetails()
maruthi.getWash()


# --------------------------------------------------------------------------------------------------------------------------------------

# multiple inheritance

class Cricketer:
    
    def __init__(self,name):
        self.name = name
        
    def play(self):
        print("I am expert in Cricket..!")
        
        
class Comedian:
    
    def __init__(self,name):
        self.name = name
        
    def playing(self):
        print("I am exprt in playing music..!")           
        
        
class Human(Cricketer,Comedian):
    
    def __init__(self,name):
        super().__init__(name)        
        
    def getDetails(self):
        super().play()    
        super().playing() 
        print("My name is ",self.name)


Sharath = Human("Sharath")


Sharath.getDetails()

# -------------------------------------------------------------------------------------------------


# multilevel inheritance

class GrandFather:
    
    def __init__(self,name):
        self.name = name
        self.money = 100000


    def work(self):
        print("I am working as Corpentor")
        
        
class Father(GrandFather):
    
    def __init__(self,name):
        super().__init__(name)
        
        
    def  getAsset(self):
        print("Our asses is ", self.money)
        

class Son(Father):
    
    def __init__(self, name):
        super().__init__(name)
        
    
    
Ram = Son("Ram")

Ram.getAsset()