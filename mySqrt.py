class Solution:
    def mySqrt(self, x: int) -> int:
        i=1
        j=x
        while i<=j:
            mid=(i+j)//2
            if pow(mid,2)>x:
                j=mid-1
            else:
                i=mid+1
        i-=1        
        return i         
        
