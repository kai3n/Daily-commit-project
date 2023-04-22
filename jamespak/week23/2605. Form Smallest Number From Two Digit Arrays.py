class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = set(nums1), set(nums2)
        if s1 & s2:
            return min(s1 & s2)
        a, b = min(nums1), min(nums2)
        return min(int(str(a) + str(b)), int(str(b) + str(a)))
