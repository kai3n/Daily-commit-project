from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def bfs(matrix,row,col):
            # 큐 선언 후 초기값 세팅
            q=[]
            q.append((row,col))
            # 섬일 경우 0으로 바꿈
            matrix[row][col] = '0'
            # 큐가 없을때까지 탐색
            while q :
                # row, col 값 선언
                r, c = q.pop(0) 
                # 상하좌우 탐색
                directions = [(1,0),(-1,0),(0,1),(0,-1)]
                for d in directions:
                    # 탐색 후 값 갱신 
                    new_r , new_c = r + d[0] , c + d[1]
                    # 탐색 한 값이 섬이면 q에 저장후 0으로 갱신
                    if 0 <= new_r < len(matrix) and 0 <= new_c < len(matrix[0]):
                        if matrix[new_r][new_c] == '1':
                            q.append((new_r,new_c))
                            matrix[new_r][new_c] = '0' 
        # 섬 개수 저장
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 섬이면 bfs실행
                if grid[i][j] == '1':
                    bfs(grid,i,j)
                    # 섬 개수 갱신
                    count += 1
        # 섬 개수 반환
        return count