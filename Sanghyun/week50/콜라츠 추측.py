def solution(num):
    for i in range(501):
        # 500까지만 반복가능함 num이 1이되면 인덱스(반복횟수) 반환
        if num == 1:
            return i
        # 짝수이면 2로 나누고 홀수이면 3을곱한후 1을 더함
        num = num/2 if num%2==0 else num*3+1
    # 500번 동안 1이 되지 않으면 -1 반환
    return -1