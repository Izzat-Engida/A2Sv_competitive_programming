class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        ans=[]
        for i in range(n):
            ans.insert(i,nums[i])
            ans.insert(i+n,nums[i])
        return ans    
