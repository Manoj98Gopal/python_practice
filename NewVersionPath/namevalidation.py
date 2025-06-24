
name = input("What is your name? ")
name_length = len(name)


if name_length < 3:
    print("Name must be at list 3 characters")
elif name_length > 10:
    print("Name can be a maximum of 10 characters")
else:
    print("Name looks good!")
    
    

