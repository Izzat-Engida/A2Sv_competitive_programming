class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=set()
        i=0
        j=0
        maxsize=0
        while j<len(s):
            if s[j] not in ans:
                ans.add(s[j])
                j+=1
                maxsize=max(len(ans),maxsize)
            else:
                ans.remove(s[i])
                i+=1
        return maxsize          

        
