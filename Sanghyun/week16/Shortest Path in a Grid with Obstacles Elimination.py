from typing import List
from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # 행렬 길이 
        m, n = len(grid), len(grid[0])

        # 데큐에 초기화 
        q = deque([(0, 0, k, 0)])
        # 봤던곳은 중복 제거
        seen = set()

        while q:
            x, y, left, steps = q.popleft()
            # 봤던곳이거나 남은 장애물이 없으면 반복 
            if (x, y, left) in seen or left < 0:
                continue
            # 도착 했으므로 steps 반환
            if (x, y) == (m - 1, n - 1):
                return steps
            # 탐색했던곳 저장 
            seen.add((x, y, left))
            # 장애물 만날경우 left갱신
            if grid[x][y] == 1:
                left -= 1
            # 상하좌우 탐색
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                # 새로운 x,y 값 저장
                new_x, new_y = x + dx, y + dy
                # 값이 m,n에 들어오면 q에 저장
                if 0 <= new_x < m and 0 <= new_y < n:
                    q.append((new_x, new_y, left, steps + 1))
        # 조건에 없으면 -1 반환
        return -1