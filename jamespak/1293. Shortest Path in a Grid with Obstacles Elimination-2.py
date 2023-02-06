from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if k >= len(grid) + len(grid[0]) - 2:
            return len(grid) + len(grid[0]) - 2
        q = deque([(0, 0, 0, 0)])
        visited = set([(0, 0, 0)])
        while q:
            x, y, obs, steps = q.popleft()
            if x == len(grid[0]) - 1 and y == len(grid) - 1:
                return steps
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if 0 <= x + dx < len(grid[0]) and 0 <= y + dy < len(grid):
                    if grid[y + dy][x + dx] == 1 and obs + 1 <= k and (x + dx, y + dy, obs + 1) not in visited:
                        visited.add((x + dx, y + dy, obs + 1))
                        q.append((x + dx, y + dy, obs + 1, steps + 1))
                    if grid[y + dy][x + dx] == 0 and (x + dx, y + dy, obs) not in visited:
                        visited.add((x + dx, y + dy, obs))
                        q.append((x + dx, y + dy, obs, steps + 1))
        return -1
