from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            # 땅 초과시 종료 
            if i < 0 or i >= len(grid) or \
                    j < 0 or j >= len(grid[0]) or \
                    grid[i][j] != '1':
                return

            grid[i][j] = 0

            # 동서남북 탐색
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        # 육지 몇개인지 저장
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 육지이면 dfs탐색
                if grid[i][j] == '1':
                    dfs(i, j)
                    # 육지 개수 갱신
                    count += 1
        # 육지 몇개인지 반환
        return count