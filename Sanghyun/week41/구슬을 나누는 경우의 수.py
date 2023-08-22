def solution(balls, share):
    # 조합 공식 이용 
    a , b = 1, 1
    for i in range(1,share+1):
        # share수만큼 ball -1을한 후 곱한 값
        a *= balls
        # 1부터 share까지 곱한 값
        b *= i
        balls -=1
    # a를 b로 나눈 후 반환 하면 서로 다른 balls을 share에게 나눠주는 방법
    return int(a/b)