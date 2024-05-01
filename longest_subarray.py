class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i=0
        j=0
        max_size=0
        change=0
        while j<len(nums):
        
            if nums[j]==0:
                change+=1
            while change>1:
                if nums[i]==0:
                    change-=1
                i+=1
            max_size=max(max_size,j-i)
            j+=1            
         
           
        return max_size             

        
