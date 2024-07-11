class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def solve(nums,path):
            if not nums:
                result.append(path)
                return
            for i in range(len(nums)):
                num=nums[i]
                temp=nums[:i] + nums[i+1:]
                print(temp)
                solve(temp,path+[num])
        solve(nums,[])
        return result            
           



        
