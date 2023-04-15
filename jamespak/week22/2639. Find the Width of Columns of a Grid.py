class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        res = []
        for column in zip(*grid):
            res.append(max(map(lambda x: len(str(x)), column)))
        return res
