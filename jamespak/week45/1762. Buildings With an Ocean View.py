class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        cur_max = 0
        res = []

        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > cur_max:
                cur_max = heights[i]
                res.append(i)
        return res[::-1]
