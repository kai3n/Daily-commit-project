import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        h = []
        for gift in gifts:
            heapq.heappush(h, -gift)
        for _ in range(k):
            heapq.heappush(h, -int(math.sqrt(-heapq.heappop(h))))
        return -sum(h)
             
