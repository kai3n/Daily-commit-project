class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        cur_max = 0
        res = []

        for i in range(1, len(heights) + 1):
            if heights[-i] > cur_max:
                cur_max = heights[-i]
                res.append(len(heights) - i)
        return res[::-1]
