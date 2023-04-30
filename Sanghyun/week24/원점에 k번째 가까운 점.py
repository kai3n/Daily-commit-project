import heapq
from typing import List

class Solution:
    # k번째 가까운 점들 출력
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for (x,y) in points:
            # 원점까지 거리 계산
            dist = x**2 + y**2
            # 거리 기준으로 힙에 추가
            heapq.heappush(heap,(dist,x,y))

        result = []
        for _ in range(k):
            # k번째까지 heap에서 pop후 result에 추가
            (dist,x,y) = heapq.heappop(heap)
            result.append((x,y))
        # 원점에서 k번째까지 가까운 점들 반환
        return result
            