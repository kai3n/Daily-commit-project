from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0

        queue = deque([(0,0,k,0)])
        visited = set([(0,0,k)])

        if k > (len(grid)-1 + len(grid[0])-1):
            return len(grid)-1 + len(grid[0])-1

        while queue:
            row, col, eliminate, steps = queue.popleft()
            if row == len(grid)-1 and col == len(grid[0])-1:
                return steps
            for new_row, new_col in [(row-1,col), (row,col+1), (row+1, col), (row, col-1)]:
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                    if grid[new_row][new_col] == 1 and eliminate > 0 and (new_row, new_col, eliminate-1) not in visited:
                        visited.add((new_row, new_col, eliminate - 1))
                        queue.append((new_row, new_col, eliminate - 1, steps + 1))
                    if grid[new_row][new_col] == 0 and (new_row, new_col, eliminate) not in visited:
                        visited.add((new_row, new_col, eliminate))
                        queue.append((new_row, new_col, eliminate, steps + 1))

        return -1
