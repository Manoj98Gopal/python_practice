# Polymarphism

# poly means many and marphism means form , something many forms 


class Dog:
    
    def getAge(self):
        print("The Dog age is 5 years")
        
        
class Cat:
    
    def getAge(self):
        print("The Cat age is 3 years")
        

class Human:
    
    def getAge(self):
        print("The human age is 10 years")
        
        
def getAnimalAge(obj):
    obj.getAge()
    
    
Prem = Human()
Tommy = Dog()
Valga = Cat()


getAnimalAge(Prem)
getAnimalAge(Tommy)
getAnimalAge(Valga)