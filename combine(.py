class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def comb(start,path):
            if len(path)==k:
                ans.append(path.copy())
            for i in range(start,n+1):
                path.append(i)
                comb(i+1,path)
                path.pop()
        comb(1,[]) 
        return ans       

        
