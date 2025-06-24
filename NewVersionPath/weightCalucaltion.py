weight = int(input("What is your weight : "))
is_lb_or_kg = input("(L)bs or (K)g : ").upper()


if is_lb_or_kg == "L":
    print(f"You are {weight / 2.20465}kg")
elif is_lb_or_kg == "K":
    print(f"Your are {weight * 2.20465} pounds")
else:
    print("I am not understand what you are telling !")