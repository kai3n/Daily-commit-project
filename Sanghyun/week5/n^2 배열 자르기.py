def solution(n, left, right):
    answer = []
    # left 부터 right+1까지 반복 
    for i in range(left, right+1):
        # i값을 n크기로 나누어서 몫과 나머지 저장한후 
        q, r = divmod(i, n)
        # 몫과 나머지 중에 큰 값과 +1을 하여 answer에 추가
        answer.append(max(q, r) + 1)
    # 새로운 1차원 배열에서 [left:right] 값들 반환 
    return answer