class Solution(object):
    def maximalSquare(self, matrix):
        if len(matrix) == 0:
            return 0
        res = 0
        dp = [[0 for j in range(len(matrix[0])+1)] for i in range(len(matrix)+1)]
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + 1
                    res = max(res, dp[i][j])
        return res**2
