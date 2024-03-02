

# creatig class
class Bikes:
    
    # constractor
    def __init__(self,name,year):
        self.name = name
        self.year = year
        
    # method of class 
    def top_speed(self,speed):
        return f"the top speed of {self.name} is {speed}"
        
        
    def model_of_bike(self):
        return f"This bike Name is {self.name} and its model {self.year}"



# creating the object
bmw = Bikes("BMW",2013)
dukati = Bikes("Dukati",2017)

# calling the class method
topSpeed = Bikes.top_speed(bmw,220)
details = Bikes.model_of_bike(dukati)




print(f"The name of bike is {dukati.name}")
print(f"The release in {dukati.year}")
print(topSpeed)
print(details)