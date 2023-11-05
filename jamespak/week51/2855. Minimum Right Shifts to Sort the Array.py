class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        peak = -1
        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % len(nums)]:
                if peak == -1:
                    peak = i
                else:
                    return -1
        return len(nums) - peak - 1
