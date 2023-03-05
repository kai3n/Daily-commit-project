def MaximizeEqualNumbers(n, k, a):
    a.sort()
    i = j = ans = 0
    while j < len(a):
        if a[i] >= a[j] - k*2:
            j += 1
        ans = max(ans, j - i)
        while j < len(a) and i < j and a[i] < a[j] - k*2:
            i += 1
    return ans
