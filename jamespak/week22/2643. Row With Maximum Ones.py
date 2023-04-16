class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_idx = 0
        max_cnt = 0
        for i, row in enumerate(mat):
            if sum(row) > max_cnt:
                max_idx = i
                max_cnt = sum(row)
        return [max_idx, max_cnt]

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        return max(enumerate(map(sum, mat)), key=lambda x:[x[1],-x[0]])
