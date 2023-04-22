class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        res = sorted(set(nums1).intersection(nums2))
        if len(res) > 0:
            return res[0]
        return min(int(str(sorted(nums1)[0]) + str(sorted(nums2)[0])), int(str(sorted(nums2)[0]) + str(sorted(nums1)[0])))
