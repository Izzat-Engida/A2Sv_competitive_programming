class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill)==2:
            return skill[0]*skill[1]
        skill.sort()
        i=0
        j=len(skill)-1
        temp=skill[i]+skill[j]
        chemi=0
        while i<=j:
            temp2=skill[i]+skill[j]
            if temp==temp2:
                chemi+=skill[i]*skill[j]
                i+=1
                j-=1
            else:
                return -1
        return chemi            

        
