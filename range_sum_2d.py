class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        i=len(matrix)
        j=len(matrix[0])
        self.prefix=[[0]*(j+1) for _ in range(i+1)]
        for r in range(i):
            for c in range(j):
                self.prefix[r+1][c+1]=self.prefix[r+1][c]+self.prefix[r][c+1]-self.prefix[r][c]+matrix[r][c]

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.prefix[row2 + 1][col2 + 1] - self.prefix[row1][col2 + 1] - self.prefix[row2 + 1][col1] + self.prefix[row1][col1])

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
