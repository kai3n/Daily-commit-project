def solution(n):
    # 1,2,4만 쓰므로 리스트에 저장 
    num = ['1','2','4']
    # 10진법을 그들의 숫자로 바꿔서 저장
    answer = ""
    # n이 0보다 클때 반복
    while n > 0:
        # 인덱스는 2까지이므로 -1 해서 갱신 
        n -= 1
        # 10진법을 124나라 진법으로 변형 
        answer = num[n % 3] + answer
        # 1,2,4 3개만 잇으므로 몫만 구함 
        n //= 3
    # 124나라 숫자로 바꾼 값 반환 
    return answer