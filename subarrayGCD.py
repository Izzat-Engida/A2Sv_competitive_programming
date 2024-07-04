class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count=0
        for i in range(len(nums)):
            temp=0
            for j in range(i,len(nums)):
                temp=gcd(temp,nums[j])
                if temp==k:
                    count+=1
                elif temp<k:
                    break
        return count                        
        
