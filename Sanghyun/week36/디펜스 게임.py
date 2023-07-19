from heapq import heappop, heappush

def solution(n, k, enemy):
    answer = 0
    sum_enemy=0
    heap = []
    # 적수 반복
    for e in enemy:
        # 최솟힙으로 푸시 
        heappush(heap, -e)
        # 적수 몇명인지 저장
        sum_enemy += e
        # 아군병력 보다 적이 많으면 k로 그 단계 넘길수 있음
        if sum_enemy > n:
            if k == 0: break
            sum_enemy += heappop(heap) 
            k -= 1
        # 몇단계인지 갱신
        answer += 1
    # 몇단계까지 클리어 했는지 반환
    return answer