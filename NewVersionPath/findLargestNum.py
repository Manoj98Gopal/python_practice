
numbers = [12,33,2,4,35,3,8,5]

large_number = 0


for num in numbers:
    if num > large_number:
        large_number = num
    

smallest_number = large_number    
    
for num in numbers:
    if num < smallest_number:
        smallest_number = num
        
        
        


print("large number is : ",large_number)
print("smallest number is :",smallest_number)