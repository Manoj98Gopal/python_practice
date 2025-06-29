number = [1,2,3,2,3,6,8,5,9,4,2,7]
unique_list = []

for num in number:
    unique_check = num in unique_list
    if not unique_check:
        unique_list.append(num)
        
        
print("result : ",unique_list)
        
            
        
