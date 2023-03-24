class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        if heights == None or len(heights) == 0 or len(heights[0]) == 0:
            return res
        n = len(heights)
        m = len(heights[0])
        pacific = [[False for _ in range(m)] for _ in range(n)]
        atlantic = [[False for _ in range(m)] for _ in range(n)]

        for i in range(n):
            self.dfs(heights, pacific, -1, i, 0)
            self.dfs(heights, atlantic, -1, i, m-1)
        for i in range(m):
            self.dfs(heights, pacific, -1, 0, i)
            self.dfs(heights, atlantic, -1, n-1, i)
        for i in range(n):
            for j in range(m):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
        return res

    def dfs(self, heights, visited, height, x, y):
        n = len(heights)
        m = len(heights[0])
        if x < 0 or x >= n or y < 0 or y >= m or visited[x][y] or heights[x][y] < height:
            return
        visited[x][y] = True
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            self.dfs(heights, visited, heights[x][y], x + dx, y + dy)
