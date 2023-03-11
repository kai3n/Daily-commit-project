class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        queue = deque()
        queue.append(start)
        visited = set()
        visited.add(tuple(start))
        while queue:
            x, y = queue.popleft()
            print(x, y, destination)
            if [x, y] == destination:
                return True
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                row = x + dx
                col = y + dy
                while 0 <= row < len(maze) and 0 <= col < len(maze[0]) and not maze[row][col]:
                    row += dx
                    col += dy
                row -= dx
                col -= dy
                if (row, col) not in visited and maze[row][col] == 0:
                    visited.add((row, col))
                    queue.append([row, col])
        return False
