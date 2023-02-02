from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # nums-1 개 반복 
        for i in range(1,len(nums)):
            # nums값을 계속 누적으로 갱신시킴 
            nums[i] += nums[i-1] if nums[i-1] > 0 else 0 
        # 갱신 시킨후 nums의 최대값을 고르면 누적해서 더한 최대값이므로 반환
        return max(nums)