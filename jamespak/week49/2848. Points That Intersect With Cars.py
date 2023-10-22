class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort()
        res = 0
        prev_start = nums[0][0]
        prev_end = nums[0][1]
        for i in range(1, len(nums)):
            if prev_end < nums[i][0]:
                res += prev_end - prev_start + 1
                prev_start = nums[i][0]
            prev_end = max(prev_end, nums[i][1])
        res += prev_end - prev_start + 1
        return res
