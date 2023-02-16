def solution(k, m, score):
    # 최고이익 반환 
    answer = 0 
    # 사과 등급을 내림차순으로 정렬 
    score = sorted(score, reverse = True)
    
    # m개가 1개의 상자에 들어가므로 건너뛰면서 반복
    for i in range(0, len(score), m):
        # m개 사과등급 저장
        temp = score[i:i+m]
        # 상자안에 갯수가 맞다면 최고이익 계산
        if len(temp) == m:
            answer += min(temp) * m
    # 최고이익 반환
    return answer