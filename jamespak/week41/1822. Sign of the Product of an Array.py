class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = reduce(lambda x, y: x * y, nums)
        if not product:
            return 0
        return 1 if product >= 1 else -1
