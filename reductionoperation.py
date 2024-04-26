class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        count=0
        for i in range(len(nums)):
            if nums[i-1]>nums[i]:
                count+=i
        return count        

        
