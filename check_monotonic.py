def chk_mon(arr): 
    if len(arr) == 0:
        return True
    f = arr[0]
    l = arr[len(arr)-1]
    
    if f == l:
        for i in range(len(arr) - 1):
            if arr[i + 1] != arr[i]: return False
    elif f < l:
        for i in range(len(arr) - 1):
            if arr[i + 1] < arr[i]: return False
    else:
        for i in range(len(arr) - 1):
            if arr[i + 1] > arr[i]: return False
    
    return True
