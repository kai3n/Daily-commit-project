class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res = -1
        s = set()
        for num in nums:
            if -num in s:
                res = max(res, abs(num))
            s.add(num)
        return res
