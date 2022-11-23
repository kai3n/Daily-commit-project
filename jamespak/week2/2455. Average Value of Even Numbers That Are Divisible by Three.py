class Solution:
    def averageValue(self, nums: List[int]) -> int:
        res = [num for num in nums if num % 6 == 0]
        return int(sum(res) / len(res)) if len(res) else 0
