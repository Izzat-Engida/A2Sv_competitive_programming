class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        ans=[]
        def comb(start,path,ta):
            if ta==0:
                ans.append(path.copy())  
                return
            if ta<0:  
                return
            for i in range(start,n):
                path.append(candidates[i])
                comb(i,path,ta-candidates[i])
                path.pop()
               
              
        comb(0,[],target) 
        return ans       

        
