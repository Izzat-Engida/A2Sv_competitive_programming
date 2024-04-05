class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        j=0
        temp=[]
        for i in range(len(s)):
            if j<len(spaces) and i==spaces[j] :
                temp.append(" ")
                j+=1
            temp.append(s[i])
        return ''.join(temp)        
