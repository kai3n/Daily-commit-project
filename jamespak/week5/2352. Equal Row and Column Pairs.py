class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d = defaultdict(int)
        res = 0
        for row in grid:
            d[",".join(map(str, row))] += 1
        for col in zip(*grid):
            if d.get(",".join(map(str, col)), 0) != 0:
                res += d.get(",".join(map(str, col)), 0)
        return res
