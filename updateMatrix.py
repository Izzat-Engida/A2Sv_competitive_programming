class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row=len(mat)
        col=len(mat[0])
        def check(i,j):
            return 0<=i<row and 0<=j<col
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        matrix=[[-1]*col for _ in range(row)] 
        q=deque()
        for i in range(row):
            for j in range(col):
                if mat[i][j]==0:
                    matrix[i][j]=0
                    q.append((i,j))
        while q:
            temp1,temp2=q.popleft()
            for a,b in directions:
                t,u=temp1+a,temp2+b
                if check(t,u) and matrix[t][u]==-1:
                    matrix[t][u]=matrix[temp1][temp2]+1
                    q.append((t,u))
        return matrix                      





        
