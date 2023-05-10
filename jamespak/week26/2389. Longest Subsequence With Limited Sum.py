class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        res = []
        for query in queries:
            max_idx = 0
            for i, num in enumerate(nums):
                if num <= query:
                    max_idx = i + 1
            res.append(max_idx)
        return res
