from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 주변 탐색 
        def dfs(i,j)  :
            # 행렬 초과 하거나 미만일시 반환 
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]!='1':
                return 
            # dfs로 들어왔으면 0으로 갱신 후 주변탐색 후 0이면 빠져나옴 
            grid[i][j] = 0 
            
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        # 섬의 개수 저장 
        count = 0
        # 행 길이 만큼 반복
        for i in range(len(grid)):
            # 열 길이 만큼 반복
            for j in range(len(grid[0])):
                # 1일때는 섬이므로 dfs로 주변 탐색 
                if grid[i][j]=='1':
                    dfs(i,j)
                    # 섬 개수 갱신 
                    count+=1
                
        #섬의 개수 반환 
        return count