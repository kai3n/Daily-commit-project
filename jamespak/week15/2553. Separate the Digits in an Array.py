class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            tmp = []
            while num >= 10:
                tmp.append(num % 10)
                num //= 10
            tmp.append(num)
            res.extend(tmp[::-1])
        return res
