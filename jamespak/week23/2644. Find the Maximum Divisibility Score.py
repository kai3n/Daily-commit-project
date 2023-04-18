class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        return max(divisors, key=lambda div:(sum([num%div==0 for num in nums]), -div))
