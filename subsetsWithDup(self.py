class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subset=[]
        sub=[]
        def solve(i):
            if i==len(nums):
                subset.append(sub.copy())
                return    
            temp=nums[i]
            sub.append(temp)
            solve(i+1)
            sub.pop()  
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            solve(i+1)  
        solve(0)
        return subset
        
