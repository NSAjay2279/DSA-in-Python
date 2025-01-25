def sqr_sort(arr):
    n = len(arr)
    res = [0] * n
    l, r = 0, n - 1
    
    for i in range(n - 1, -1, -1):
        ls, rs = arr[l] ** 2, arr[r] ** 2
        if ls > rs:
            res[i] = ls
            l += 1
        else:
            res[i] = rs
            r -= 1
    return res
