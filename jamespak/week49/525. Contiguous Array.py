class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = res = 0
        d = {0: -1}
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            if count in d:
                res = max(res, i - d[count])
            else:
                d[count] = i
        return res
