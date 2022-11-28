class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = n*(n + 1) / 2
        cur_sum = 0
        for num in range(1, n + 1):
            cur_sum += num
            if cur_sum*2 == total_sum + num:
                return num
        return -1
