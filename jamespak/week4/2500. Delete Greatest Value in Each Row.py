class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid : row.sort(reverse=True)
        return sum(max(col) for col in zip(*grid))
