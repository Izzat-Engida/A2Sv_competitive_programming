class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        countp=Counter(p)
        counts=Counter(s[:len(p)-1]) 
        ans=[]
        i=len(p)-1
        while i<len(s):
            counts[s[i]]+=1
            if countp==counts:
                ans.append(i-len(p)+1)
            counts[s[i-len(p)+1]] -= 1  
            if counts[s[i-len(p)+1]] == 0:
                del counts[s[i-len(p)+1]] 
            i+=1
        return ans                           
       
