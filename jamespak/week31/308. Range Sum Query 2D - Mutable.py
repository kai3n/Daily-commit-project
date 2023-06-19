class NumMatrix(object):

    def __init__(self, matrix):
        self.d = matrix
        for row in matrix:
            for i in range(1, len(row)):
                row[i] += row[i-1]

    def update(self, row, col, val):
        row = self.d[row]
        orig = row[col] - (row[col-1] if col else 0)
        for i in range(col, len(row)):
            row[i] += val - orig

    def sumRegion(self, row1, col1, row2, col2):
        out = 0
        for i in range(row1, row2+1):
            out += self.d[i][col2] - (self.d[i][col1-1] if col1 else 0)
        return out
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
