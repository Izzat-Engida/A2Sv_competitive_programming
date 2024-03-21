class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        r=len(matrix)
        c=len(matrix[0])
        tmatrix=[[0]*r for _ in range(c)]
        for i in range(r):
            for j in range(c):
                tmatrix[j][i]=matrix[i][j]
        return tmatrix        
