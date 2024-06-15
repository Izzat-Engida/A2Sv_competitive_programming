class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)
        while left<=right:
            mid=left+(right-left)//2
            if self.check(weights,days,mid):
                right=mid-1
            else:
                left=mid+1
        return left      
    def check(self,weights,days,capacity):
        day=1
        wei=0
        for w  in weights:
            if wei+w<=capacity:
                wei+=w
            else:
                day+=1
                wei=w
        return day<=days                        
        
