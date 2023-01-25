from typing import List
class Solution:
    # 행렬에서 target값 찾기 
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # matrix가 없으면 False반환 
        if not matrix:
            return False
        # 행,열 초기화 
        row = 0
        col = len(matrix[0]) - 1

        # row 행 길이보다 작고 col가 0보다 크면 반복  
        while row <= len(matrix) - 1 and col >= 0:
            # target값이 일치하면 True반환 
            if target == matrix[row][col]:
                return True
            # target값이 작으면 같은행이므로 col만 갱신 
            elif target < matrix[row][col]:
                col -= 1
            # target값이 크면 다음 행이므로 행만 갱신 
            elif target > matrix[row][col]:
                row += 1
        # target값이 없으면 False 반환 
        return False