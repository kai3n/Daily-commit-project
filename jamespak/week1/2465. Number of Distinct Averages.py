class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        s = set()
        l = 0
        r = len(nums) - 1
        while l < r:
            s.add((nums[l] + nums[r]) / 2)
            l += 1
            r -= 1
        return len(s)
