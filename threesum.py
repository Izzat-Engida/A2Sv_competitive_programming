class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        temp=set()

        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while j<k:
                sums=nums[i]+nums[j]+nums[k]
                if sums==0:
                    temp.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif sums<0:
                    j+=1
                else:
                    k-=1
       
        return temp                        
        
