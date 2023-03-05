def solve(N, A):
    ans = N*(N + 1)//2
    connected_ones = sorted("".join(list(map(str, A))).replace("0"," ").split(), key=lambda x:len(x), reverse=True)
    for i in range(len(connected_ones)):
        if i == 0:
            if len(connected_ones[i]) % 2:
                n = len(connected_ones[i]) // 2
                ans -= n * (n + 1)
            else:
                if len(connected_ones[i]) == 2:
                    ans -= 1
                else:
                    n = len(connected_ones[i]) // 2
                    ans -= (n * (n + 1)//2 + n * (n - 1)//2)
        else:
            n = len(connected_ones[i])
            ans -= n*(n + 1) // 2
    return ans
