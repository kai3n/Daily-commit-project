class Solution:
    def maxJump(self, A):
        res = A[1] - A[0];
        for i in range(2, len(A)):
            res = max(res, A[i] - A[i - 2])
        return res
