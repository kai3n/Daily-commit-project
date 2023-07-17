class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        l = len(nums)
        res = 0
        for i in range(len(nums)):
            if l % (i + 1) == 0:
                res += nums[i]**2
        return res
