
condition  = True
count = 0
is_car_started = False

while condition:
    user_input = input("> ").upper()
    
    if user_input == "HELP":
        print('''
start - to start car 
stop - to stop car 
quit - to exit
              ''')
    elif user_input == "START":
        if is_car_started :
            print("Car is Already started ..!")
        else:
            print("Car is started")
        is_car_started = True
    elif user_input == "STOP":
        if not is_car_started:
            print("Car is Already stopped")
        else:
            print("Car stopped..")
        is_car_started = False
    elif user_input == "QUIT":
        break
    else:
        print("I dont understand !")
    