class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row=len(image)
        col=len(image[0])
        temp=image[sr][sc]
        if temp==color:
            return image
        directions=[(-1,0),(0,-1),(1,0),(0,1)]
        def check(i,j):
            return 0<=i<row and 0<=j<col
        visited=set()
        def dfs(image,temp1,temp2):
            if (temp1,temp2) not in visited:
                visited.add((temp1,temp2))
                image[temp1][temp2]=color
                for a,b in directions:
                    t,u=temp1+a,temp2+b
                    if check(t,u) and image[t][u]==temp:
                        dfs(image,t,u)

        dfs(image,sr,sc)          
        return image         




        
