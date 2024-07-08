class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n=len(nums)
        i=0
        while i<n:
            c=nums[i]-1
            if nums[i]!=nums[c]:
                nums[i],nums[c]=nums[c],nums[i]
            else:
                i+=1
        answer=[]        
        for i in range(n):
            if nums[i]-1 !=i:
                answer.append(nums[i])
        return answer        
                            
    
    

        
