from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            # 땅이 아니면 종료 
            if i < 0 or i >= len(grid) or \
                    j < 0 or j >= len(grid[0]) or \
                    grid[i][j] != '1':
                return
            # 탐색 한곳은 0으로 갱신 
            grid[i][j] = 0

            # 동서남북 탐색
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # 육지 개수 저장 
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 땅일 경우 탐색 
                if grid[i][j] == '1':
                    dfs(i, j)
                    # 탐색 후 육지 개수 갱신
                    count += 1
        # 육지 개수 반환
        return count