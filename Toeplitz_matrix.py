class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(n):
                row=i-1
                col=j-1
                if 0<=row<m and 0<=col <n and matrix[row][col]!=matrix[i][j]:
                    return False
        return True
            
