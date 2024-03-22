class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        newm = [[0]*(n-2) for _ in range(n-2)]
        for i in range(1, n-1):
            for j in range(1, n-1):
                m = max(
                    grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1],
                    grid[i][j-1], grid[i][j], grid[i][j+1],
                    grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1]
                )
                newm[i-1][j-1] = m
        return newm
