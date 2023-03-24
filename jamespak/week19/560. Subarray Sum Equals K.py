class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = collections.Counter()
        count[0] = 1
        res = prefix_sum = 0
        for num in nums:
            prefix_sum += num
            res += count[prefix_sum - k]
            count[prefix_sum] += 1
        return res
