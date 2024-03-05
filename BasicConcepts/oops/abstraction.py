
# abstract method means, a method doesn't have body is called abstract method , a class have 
# have abstract method is called abstract class
# It helps to hiding the complex implementation and only it is showing neccessary information


from abc import ABC,abstractmethod



class Vhicle(ABC):
    
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
    
class Car(Vhicle):
    
    def start(self):
        print(f'{self.make} {self.model} ({self.year}) is starting.....')
        
    def stop(self):
        print(f'{self.make} {self.model} ({self.year}) is stoped.....')
        
        
class Scooter(Vhicle):
    
    def start(self):
        print(f'{self.make} {self.model} ({self.year}) is starting.....')
        
    def stop(self):
        print(f'{self.make} {self.model} ({self.year}) is stoped.....')
        
        

maruthi = Car("Maruthi","swift",2018)
splender = Scooter("Hero","Ismart",2016)


maruthi.start()
splender.stop()