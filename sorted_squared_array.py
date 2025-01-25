def sorted_squared_array(array):
    for i in range(len(array)):
        array[i] = array[i] * array[i]
    
    newarray = [0] * len(array)
        
    lptr = 0
    rptr = len(array) - 1
    for i in range(len(array)):
        if array[lptr] > array[rptr]:
            newarray[rptr] = array[lptr]
            lptr += 1
        else:
            newarray[rptr] = array[rptr]
            rptr -= 1
    
    return newarray
            