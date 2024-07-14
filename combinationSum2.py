class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n=len(candidates)
        ans=[]
        def comb(start,path,ta):
            if ta==0:
                ans.append(path.copy())  
                return
            if ta<0:  
                return
            prev=-1    
            for i in range(start,n):
                if prev==candidates[i]:
                    continue
                path.append(candidates[i])
                comb(i+1,path,ta-candidates[i])
                path.pop()
                prev=candidates[i]
               
        comb(0,[],target) 
        return ans       
        
