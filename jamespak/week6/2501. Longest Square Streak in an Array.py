class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        d = defaultdict(int)
        nums = list(set(nums))
        nums.sort()
        res = -1
        for num in nums:
            d[num] = 1

        for num in nums:
            if d[num*num] != 0:
                d[num*num] += d[num]
                res = max(res, d[num*num])
        return res
