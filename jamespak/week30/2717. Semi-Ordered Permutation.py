class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        a = nums.index(1)
        b = nums.index(len(nums))
        if a < b:
            return a + len(nums) - b - 1
        else:
            return a + len(nums) - b - 2
