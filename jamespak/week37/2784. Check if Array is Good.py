class Solution:
    def isGood(self, nums: List[int]) -> bool:
        return Counter(nums) == Counter(range(1, len(nums))) + Counter((len(nums) - 1,))
