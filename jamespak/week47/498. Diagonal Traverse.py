class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = []
        dd = defaultdict(list)
        if not mat: 
            return result

        for i in range(0, len(mat)):
            for j in range(0, len(mat[0])):
                dd[i + j + 1].append(mat[i][j])

        for k, v in dd.items():
            if k%2 == 1: 
                dd[k].reverse()
            result += dd[k]
        return result
