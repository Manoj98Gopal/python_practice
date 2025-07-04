
def find_large_num(array):
    temp_array = array
    large_num = array[0]
    
    for num in temp_array:
        if num > large_num:
            large_num = num
            
    return large_num


def find_small_num(array):
    temp_array = array
    small_num = array[0]
    
    for num in temp_array:
        if num < small_num:
            small_num = num
            
    return small_num
