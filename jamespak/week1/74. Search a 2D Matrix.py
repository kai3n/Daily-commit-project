class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first = 0
        last = len(matrix)*len(matrix[0])
        while first < last:
            mid = (first + last) // 2
            r = mid // len(matrix[0])
            c = mid % len(matrix[0])
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                first = mid + 1
            else:
                last = mid
        return False
