class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ma=float('-inf')
        i=0
        j=k
        su=0
        while i<j and i<len(nums):
            su+=nums[i]
            i+=1
        ma=max(ma,su/k)
         
        while j<len(nums) and i<len(nums):
            
            su-=nums[i-k]
            su+=nums[j]
            i+=1
            j+=1
           
            ma=max(ma,su/k)
        return ma    
            




        
