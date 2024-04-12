class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ma=0
        total=0
        for i in range(k):
            total+=nums[i]
        ma=total/k
        r=k
        l=0
        while r<len(nums):
            total-=nums[l]
            total+=nums[r]
            r+=1
            l+=1
            ma=max(ma,total/k)
        return ma        


        
