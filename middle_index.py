class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left,right=0,0
        for i in nums:
            right+=i
        for i in range(len(nums)):
            right-=nums[i]
            if left==right:
                return i
            left+=nums[i]
        return -1           
