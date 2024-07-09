class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        def check(i,j):
            return 0<=i<row and 0<=j<col
        visit=set() 
        directions=[(0,-1),(0,1),(1,0),(-1,0)]   
        def dfs(i,j):
            if not check(i, j) or grid[i][j] == 0 or (i, j) in visit:
                return 0
            count=1
            if check(i,j) and grid[i][j]==1 and (i,j) not in visit:
                visit.add((i,j))
                for a,b in directions:
                    temp1,temp2=i+a,j+b
                    count+=dfs(temp1,temp2)
            return count        
        count=0    
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1 and (i,j) not in visit:
                    count=max(dfs(i,j),count)
        return count                


        
