from typing import List
import heapq

class Solution:
    #  k번 가까운 점 목록을 순서대로 출력 
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #  선언 
        heap = []
        # x,y 값 추출 
        for (x,y) in points:
            # 유클리드 거리 계산 
            dist = x**2 + y**2
            # 힙에 삽입 
            heapq.heappush(heap,(dist,x,y))
        # 출력 할 x,y저장공간 
        result = []
        # k만큼 반복 
        for _ in range(k):
            # 최소 힙이므로 거리가 제일 가까운 순으로 반환 
            (dist,x,y) = heapq.heappop(heap)
            # x,y좌표 result에 저장 
            result.append((x,y))
        # k번 가까운 점 목록을 순서대로 반환 
        return result