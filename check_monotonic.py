def check_monotonic(array):
   
    MD = True
    MI = True

    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] <= array[j]:
                break;
            else:
                MI = False
    
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] >= array[j]:
                break;
            else:
                MD = False

    if MD == True:
        return True
    elif MI == True:
        return True
    else:
        return False

print(checkMonotonic([1,2,3,2]))
print(checkMonotonic([3,2,2,1]))
print(checkMonotonic([1,2,3,4]))