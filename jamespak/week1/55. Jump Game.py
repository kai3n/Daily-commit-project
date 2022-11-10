class Solution:
    def canJump(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            nums[i + 1] = max(nums[i + 1], nums[i] - 1)
            if nums[i] == 0:
                return False
        return True
