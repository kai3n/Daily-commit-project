def solution(l, r):
    answer = []
    for i in range(l, r+1):
        # i에서 0,5로 이루어진 모든 정수 저장
        if all(num in ['0', '5'] for num in str(i)):
            answer.append(i)
    # answer이 0이면 -1 반환 
    if len(answer) == 0:
        answer.append(-1)
    # 오름차순으로 저장된 값들 반환
    return answer