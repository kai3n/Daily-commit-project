class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return 0

        d = defaultdict(int)
        cur_sum = res = 0

        for i in range(len(nums)):
            cur_sum += nums[i]
            d[nums[i]] += 1
            if i >= k:
                cur_sum -= nums[i - k]
                d[nums[i - k]] -= 1
                if d[nums[i - k]] <= 0:
                    del d[nums[i - k]]
            if len(d) == k:
                res = max(res, cur_sum)
        return res
        
