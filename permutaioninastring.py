class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i=0
        le=len(s1)
        j=le-1
        while j<len(s2):
            if Counter(s1)==Counter(s2[i:j+1]):
                return True
            else:
                i+=1
                j+=1
        return False            

        
