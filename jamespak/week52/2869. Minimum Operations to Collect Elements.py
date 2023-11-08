class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        s = {x for x in range(1, k + 1)}
        for num in nums[::-1]:
            res += 1
            if num in s:
                s.remove(num)
            if len(s) == 0:
                return res
        return res
