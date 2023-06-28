class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        d = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                d[mat[i][j]].append([i, j])
        dp = [[0] * len(mat[0]) for _ in range(len(mat))]
        rm = [0] * len(mat)
        cm = [0] * len(mat[0])
        for k in sorted(d):
            for i, j in d[k]:
                dp[i][j] = max(rm[i], cm[j]) + 1
            for i, j in d[k]:
                rm[i] = max(rm[i], dp[i][j])
                cm[j] = max(cm[j], dp[i][j])
        return max(rm + cm)
