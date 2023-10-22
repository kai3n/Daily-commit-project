def solution(n):
    
    def hanoi(n, src, to, mid):
        # n이 1일때 출발지 도착지 저장
        if n == 1:
            answer.append([src, to])
            return
        # 처음 원판을 중간으로 옮김
        hanoi(n - 1, src, mid, to)
        # 두번째 원판을 도착지로 옮김
        answer.append([src, to])
        # 중간 원판을 도착지로 옮김
        hanoi(n - 1, mid, to, src) 
        
    answer = []
    # 원판개수, 출발지, 도착지, 중간지점으로 재귀로 저장
    hanoi(n, 1, 3, 2)
    return answer