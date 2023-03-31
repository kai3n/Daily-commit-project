import collections
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # num 빈도수 계산 
        freqs = collections.Counter(nums)
        heap = []
        # 힙에 음수로 저장
        for f in freqs:
            heapq.heappush(heap, (-freqs[f], f))
        # 상위 빈도수 리스트
        top_k =[]
        # k번 만큼 반복후 가장 작은 음수 순으로 저장
        for _ in range(k):
            top_k.append(heapq.heappop(heap)[1])
        # 상위 k 빈도수 반환
        return top_k