class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = defaultdict(int)
        d[0] = -1
        total = 0
        for i, num in enumerate(nums):
            total = (total + num) % k
            if total not in d:
                d[total] = i
            else:
                if i - d[total] >= 2:
                    return True
        return False
