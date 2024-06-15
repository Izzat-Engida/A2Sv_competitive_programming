class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        while left<=right:
            mid= (right+left)//2
            if self.check(piles,mid,h):
                right=mid-1
            else:
                left=mid+1
        return left            

    def check(self,piles,k,h):
        hours=0
        for p in piles:
            hours+= -(-p//k)
        return hours<=h    
