def solution(n):
    # 첫번쨰와 두번째는 0,1로 갱신 후 n-1개만큼 0으로 갱신 
    result = [0,1] + [0]*(n-1)
    # 2부터 n+1까지 반복 
    for i in range(2,n+1):
        # result 값 갱신 
        result[i] += result[i-2] + result[i-1]
    # 마지막값을 꺼낸 후 /1234567 한후 반환
    return (result.pop())%1234567