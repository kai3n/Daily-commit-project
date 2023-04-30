class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        res = 0
        for num in range(max(nums), max(nums) + k):
            res += num
        return res
