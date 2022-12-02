def solution(n):
    # n+1개 까지 점화식을 위해서 리스트 0값 갱신 
    temp =[0]*(n+1)
    # 초기값 설정 
    temp[0] = 1
    temp[1] = 1
    # 인덱스 3은 인덱스 1, 인덱스 2 더한 값
    for i in range(2,n+1):
         temp[i] = (temp[i-2]+temp[i-1])%1234567
    # 맨 마지막 값을 반환 
    return temp[-1]