class Solution(object):
    def canMeasureWater(self, x, y, z):
        if x + y < z: 
            return False
        visited, queue = set(), deque([(0, 0)])
        while queue:
            i, j = queue.popleft()
            visited.add((i, j))
            if i + j == z: 
                return True
            moves = set([
                (x, j), (i, y), (0, j), (i, 0),
                (min(i + j, x), (i + j) - min(i + j, x)),
                ((i + j) - min(i + j, y), min(i + j, y)),
            ])
            queue.extend(moves - visited)
        return False
