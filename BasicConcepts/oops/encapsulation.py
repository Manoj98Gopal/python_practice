
# Encapsulation is bundling the  data and methods in single unit or class,
# Encapsulation is helps to hide internal state and implementation of object from out side world
# It helps to better modularity, reusability and maintainability


class Bank_Acc:
    
    # constractore
    def __init__(self,accNo,balance):
        
        self.account_number = accNo        #public variable
        self.__account_balance = balance   #private variable
        
    def get_balance(self):
        print("Your balance is :- ",self.__account_balance)
        
    # modifiying the private variable 
    def deposit(self,amount):
        self.__account_balance = self.__account_balance + amount
       
    def withDraw(self,amount):
        if self.__account_balance > amount:
            self.__account_balance = self.__account_balance - amount
            print("with draw amount from your account =",amount)    
        else:
            print("Insuffisent bank balance")



# creating object
manoj = Bank_Acc("12345",10000)




manoj.get_balance()
manoj.deposit(500)
manoj.get_balance()
manoj.withDraw(5000)
manoj.get_balance()
