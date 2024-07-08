class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indgree=[0]*n
        for _,b in edges:
            indgree[b]+=1
        answer=[]
        for i in range(n):
            if indgree[i]==0:
                answer.append(i)
        return answer            
        
