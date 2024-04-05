class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i=0
        j=int(c**0.5)
        while i<=j:
            su=i**2 +j**2
            if su==c:
                return True
            elif su>c:
                j-=1
            else:
                i+=1
        return False        

            
        
