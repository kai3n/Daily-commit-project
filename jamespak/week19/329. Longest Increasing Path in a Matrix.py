class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i - 1, j) if 0 <= i - 1 < M and val > matrix[i - 1][j] else 0,
                    dfs(i + 1, j) if 0 <= i + 1 < M and val > matrix[i + 1][j] else 0,
                    dfs(i, j - 1) if 0 <= j - 1 < N and val > matrix[i][j - 1] else 0,
                    dfs(i, j + 1) if 0 <= j + 1 < N and val > matrix[i][j + 1] else 0)
            return dp[i][j]

        if not matrix or not matrix[0]: return 0
        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for i in range(M)]
        return max(dfs(x, y) for x in range(M) for y in range(N))
