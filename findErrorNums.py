class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        i=0
        answer=[]
        while i<n:
            c=nums[i]-1
            if nums[c]!=nums[i]:
                nums[i],nums[c]=nums[c],nums[i]
            else:
                i+=1
        for i in range(n):
            if i!=nums[i]-1:
                m=i+1
                answer.append(nums[m-1])
                answer.append(m)
        return answer        

        
