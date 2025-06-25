secrete_Num = 9

chance = 0

while chance < 3:
    Guess_number = int(input("Guess : "))
    chance += 1
    if Guess_number == secrete_Num:
        print("Your win !")
        break
else:
    print("Sorry You Failed !")
        
