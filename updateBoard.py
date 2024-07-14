class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row=len(board)
        col=len(board[0])
        def check(i,j):
            return 0<=i<row and 0<=j<col
        temp1,temp2=click
       
        di=[(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,1),(-1,-1),(1,-1)]
        def dfs(i,j):
            if not check(i,j) or board[i][j]!='E':
                return 
            count=0
            if board[i][j]=='M':
                board[i][j]='X'
                return 
            if board[i][j]=='E':   
                for a,b in di:
                    t,u=a+i,b+j
                    if check(t,u) and board[t][u]=='M':
                        count+=1
            if count>0:
                board[i][j]=str(count)
            else:
                board[i][j]='B'
                for a,b in di:
                    dfs(i+a,b+j)
        if board[temp1][temp2]=='M':
            board[temp1][temp2]='X' 
        else:
            dfs(temp1,temp2)                 

        return  board  

                  
        
