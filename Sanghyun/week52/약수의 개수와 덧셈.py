def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        # 제곱근이면 그 수는 약수가 홀수이므로 마이너스 짝수이면 플러스
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    # left 와 right 사이 값이 약수가 홀수이면 마이너스 짝수이면 플러스한 값 반환
    return answer