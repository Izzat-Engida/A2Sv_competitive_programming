class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        j=0
        mi=len(nums)+1
        su=0    
        while j<len(nums):
            su+=nums[j]
            while su>=target:
                le=j-i+1
                mi=min(le,mi)
                su-=nums[i]
                i+=1
            j+=1
        return mi if mi<=len(nums) else 0        
                
        
