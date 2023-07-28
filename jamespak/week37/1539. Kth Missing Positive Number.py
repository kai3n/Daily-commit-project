# O(N)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr_set = set(arr)
        for i in range(1, k + len(arr) + 1):
            if i not in arr_set:
                k -= 1
            if k == 0:
                return i
# O(logN)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l , r = 0, len(arr) # 0 1
        while l < r:
            m = (l + r) // 2
            if arr[m] - m - 1 < k:
                l = m + 1
            else:
                r = m
        return r + k
