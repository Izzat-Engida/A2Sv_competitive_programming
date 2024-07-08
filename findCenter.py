class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
       temp1=edges[0][0]
       temp2=edges[0][1]
       temp3=edges[1][0]
       temp4=edges[1][1]
       if(temp1==temp3 or temp1==temp4):return temp1
      
       if(temp2==temp3 or temp2==temp4 ):return temp2
       
       return -1
        

        
