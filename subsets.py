class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset=[]
        sub=[]
        def solve(i):
            if i==len(nums):
                subset.append(sub.copy())
                return
            temp=nums[i]
            solve(i+1)
            sub.append(temp)
            solve(i+1)
            sub.pop()    
        solve(0)
        return subset   



