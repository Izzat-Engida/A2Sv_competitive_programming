class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        def move(a,n):
            i=ord(a)-ord('a')
            i=(i+n)%26
            if i<0:
                i=i+26
            return chr(ord('a') + i)  
        n=len(s)
        prefixsum=[0]*(n+1)
        for a,b,c in shifts:
            if c==0:
                prefixsum[a]-=1
                prefixsum[b+1]+=1
            else:
                prefixsum[a]+=1
                prefixsum[b+1]-=1
        for i in range(1,len(prefixsum)): 
            prefixsum[i]+=prefixsum[i-1]
        ans=""
        for i in range(n):
            ans+=move(s[i],prefixsum[i])
        return ans               



        
