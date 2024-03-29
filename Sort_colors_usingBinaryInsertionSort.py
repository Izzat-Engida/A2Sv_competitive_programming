class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(1,len(nums)):
            j=i-1
            key=nums[i]
            pos=self.binary_search(nums,0,j,key)
            while j>=pos:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=key
    def binary_search(self,nums,low,high,key):
        if high<=low:
            return low+1 if nums[low]<key+1 else low
        mid=(high+low)//2
        if nums[mid]==key:
            return mid
        if nums[mid]<key:
            return self.binary_search(nums,mid+1,high,key)
        return self.binary_search(nums,low,mid-1,key)                        
