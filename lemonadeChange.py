class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c5=0
        c10=0
        c20=0
        for i in bills:
            if i==5:
                c5+=1
            elif i==10:
                if c5<1:
                    return False
                c10+=1
                c5-=1
            elif i==20:
                if c5>=1 and c10>=1:
                    c5-=1
                    c10-=1
                    c20+=1
                elif c5>=3:
                    c5-=3
                else:
                    return False
        return True                           
        
