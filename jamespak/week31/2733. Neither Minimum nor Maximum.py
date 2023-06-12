class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        a = b = c = 0
        for n in nums:
            if n > a:
                a, b, c = n, a, b
            elif n > b:
                b, c = n, b
            elif n > c:
                c = n
            if a > b > c and c != 0:
                return b
        return -1
