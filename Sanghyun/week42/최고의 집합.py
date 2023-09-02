from math import ceil

def solution(n, s):
    # n이 s보다 크면 나눌수 없으므로 -1 반환
    if n > s : 
        return [-1]
    
    answer = []
    
    for i in range(n):
        # 홀수일경우 올림해서 값 저장
        answer.append(ceil(s/(n-i)))
        # 초기 s값에서 저장한 수만큼 빼서 갱신
        s -= ceil(s/(n-i))
    # 각 원소의 곱이 최대가 되는 두수 반환
    return sorted(answer)