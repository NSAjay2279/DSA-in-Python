def sorted_squared_array(array):
    new_array = [0] * len(array)
    pointer_left = 0
    pointer_right = len(array) - 1
    
    for i in range(len(array) - 1, -1, -1):
        left_squared = array[pointer_left] ** 2
        right_squared = array[pointer_right] ** 2
        
        if left_squared > right_squared:
            new_array[i] = left_squared
            pointer_left += 1
        else:
            new_array[i] = right_squared
            pointer_right -= 1
    
    return new_array
