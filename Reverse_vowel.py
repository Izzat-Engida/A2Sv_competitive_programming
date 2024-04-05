class Solution:
    def reverseVowels(self, s: str) -> str:
        def is_vowel(c):
            return c in 'aeiouAEIOU'
        s=list(s)
        i=0
        j=len(s)-1
        while i<j:
            if not is_vowel(s[i]):
                i+=1
                continue
            if not is_vowel(s[j]):
                j-=1
                continue
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        return ''.join(s)                
        
