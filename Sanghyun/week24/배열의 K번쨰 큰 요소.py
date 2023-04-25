from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 내림 차순으로 정렬후 k번쨰 큰 요소 반환
        return sorted(nums, reverse=True)[k - 1]