number_map = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine",
    "0" : "Zero",
}


phone_number = input("Phone number : ")

result = ""

for num in phone_number:
    result = result + " " + number_map[num]
    
print("result : ",result)