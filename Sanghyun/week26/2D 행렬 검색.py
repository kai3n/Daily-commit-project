class Solution:
    def searchMatrix(self, matrix, target):
        # 행렬 없으면 False반환
        if not matrix:
            return False

        # 행렬 인덱스 설정
        row = 0
        col = len(matrix[0]) - 1
        # 타겟 있으면 True 없으면 False 바ㄴ환 
        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            # 타겟이 작으면 열에서 왼쪽으로 한칸씩 이동
            elif target < matrix[row][col]:
                col -= 1
            # 타겟이 크면 행을 아래로 한칸씩 이동
            elif target > matrix[row][col]:
                row += 1
        return False