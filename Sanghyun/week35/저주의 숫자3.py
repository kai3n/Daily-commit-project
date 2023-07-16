def solution(n):
    # 결과값반환
    answer = 0
    for _ in range(n):
        # 반복수 저장
        answer += 1
        # answer가 3의 배수 또는 '3'이 있으면 다음 수 저장
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    # 3의 배수 또는 '3'이 없는 정수들 변환한 값 반환
    return answer
