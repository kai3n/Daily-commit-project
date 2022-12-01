def solution(n):
    # 건전지 사용량 저장
    count = 0
    while n >0:
        # n을 2로 나누어서 떨어지면 순간이동으로 가서 건전지 사용량이 없음
        a,b = divmod(n,2)
        # 2로 나눈 몫을 다시 n에 저장
        n = a 
        # 나머지가 1이면 점프 해야하므로 건전지 1소비
        if b!=0:
            count+=1
    # 최소 건전지 사용량 반환
    return count