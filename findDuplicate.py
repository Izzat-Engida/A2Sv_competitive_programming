class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        while i<n:
            c=nums[i]-1
            if nums[i]!=nums[c]:
                nums[c],nums[i]=nums[i],nums[c]
            else:
                i+=1
        for i in range(n):
            if nums[i]-1 !=i:
                return nums[i]
        return None                    
        
