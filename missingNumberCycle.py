class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        for i in range(n):
            while 0<=nums[i]<n and nums[i]!=i:
                c=nums[i]
                if nums[i]!=nums[c]:
                    nums[i],nums[c]=nums[c],nums[i]
              
        for i in range(n):
            if i!=nums[i]:
                return i
        return n                
           
           
