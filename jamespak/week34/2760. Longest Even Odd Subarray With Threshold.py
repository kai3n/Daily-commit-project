class Solution:
  def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
    res = 0
    for l in range(len(nums)):
      if nums[l] % 2 == 0 and nums[l] <= threshold:
        r = l
        while r + 1 < len(nums) and nums[r + 1] <= threshold and nums[r] % 2 != nums[r + 1] % 2:
          r += 1
        res = max(res, r - l + 1)

    return res
