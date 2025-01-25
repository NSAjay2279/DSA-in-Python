def sqr_sort(arr):
    n = len(arr)
    narr = [0] * n
    lp, rp = 0, n - 1
    
    for i in range(n - 1, -1, -1):
        ls, rs = arr[lp] ** 2, arr[rp] ** 2
        if ls > rs:
            narr[i] = ls
            lp += 1
        else:
            narr[i] = rs
            rp -= 1
    return narr
