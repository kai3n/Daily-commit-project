import heapq

def solution(n, works):
    # 야근 할일이 없으면 0반환
    if sum(works) <= n:
        return 0
    # heapq은 최소힙이므로 음수로 최대힙으로 저장
    works = [-work for work in works]
    heapq.heapify(works)
    for _ in range(n):
        # 최대힙 뽑아내고 음수이므로 +1해서 줄이고 다시 힙에 넣음
        value = heapq.heappop(works)
        value +=1
        heapq.heappush(works,value)
    # 하루 야근시간 당 제급해서 다 더한후 반환
    return sum([w**2 for w in works])
