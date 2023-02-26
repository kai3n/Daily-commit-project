class Solution(object):
    def leftRigthDifference(self, nums):
        prefix, suffix = 0, sum(nums)
        res = []
        for num in nums:
            suffix -= num
            res.append(abs(prefix - suffix))
            prefix += num
        return res
