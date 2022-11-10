class Solution:
    def jump(self, nums: List[int]) -> int:

        minJump= cur_farthest = prev_farthest = 0

        for i in range(len(nums) - 1):
            cur_farthest = max(cur_farthest, nums[i] + i)
            if  prev_farthest == i:
                prev_farthest = cur_farthest
                minJump += 1
        return minJump
