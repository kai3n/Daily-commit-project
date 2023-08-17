class Solution:
    def maxSum(self, nums: List[int]) -> int:
        res, d = -1, defaultdict(int)
        for n in nums:
            maxD = max(str(n))
            if d[maxD]: 
                res = max(res, n + d[maxD])
            d[maxD] = max(n, d[maxD])
        
        return res
