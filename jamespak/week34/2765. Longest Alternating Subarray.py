class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        i = j = 0

        while i < n:
            j = i + 1
            while j < n and nums[j] == nums[i] + (j - i)%2:
                res = max(res, j - i + 1)
                j += 1
            i = max(i + 1, j - 1)
        return res if res > 1 else -1
