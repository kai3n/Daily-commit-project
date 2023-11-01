class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        
        min_sum = float('inf')
        left_min = [nums[0]] * len(nums)
        right_min = [nums[-1]] * len(nums)
        
        for i in range(1, len(nums)):
            left_min[i] = min(left_min[i-1], nums[i])

        for i in range(len(nums) - 2, -1, -1):
            right_min[i] = min(right_min[i+1], nums[i])

        for i in range(1, len(nums) - 1):
            if(nums[i] > left_min[i] and nums[i] > right_min[i]):
                min_sum = min(min_sum , left_min[i] + nums[i] + right_min[i])
                
                
        if(min_sum != float("inf")):
            return min_sum
        else:
            return -1
