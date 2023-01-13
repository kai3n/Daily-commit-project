class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        h = []
        for num in nums:
            heapq.heappush(h, -num)
        i = 0
        while i < k: 
            cur_high = heapq.heappop(h)
            score -= cur_high 
            heapq.heappush(h, -math.ceil(-cur_high / 3.0))
            i += 1
        return score
