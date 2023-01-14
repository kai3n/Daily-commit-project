import heapq
from typing import List
class Solution:
    # 리스트에서 k번쨰로 큰 수 반환 
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 리스트로 선언 
        heap = list()
        for n in nums:
            # heapq은 최소힙만 지원하므로 n값을 마이너스로 저장해서 최대힙으로 변환 
            heapq.heappush(heap, -n)
        # k-1번까지 반복
        for _ in range(1, k):
            # k-1번째 pop을 해서 k번째가 루트노드에 있도록 함
            heapq.heappop(heap)
        # 최대힙 구현을 위대서 마이너스로 저장했으므로 다시 원복 후 반환 
        return -heapq.heappop(heap)