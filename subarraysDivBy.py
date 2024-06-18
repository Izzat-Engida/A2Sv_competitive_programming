class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count=0
        sums=0
        run={0:1}
        
        for num in nums:
            sums+=num
            temp=sums%k
            if temp<0:
                temp+=k
            if temp in run:
                count+=run[temp]
            run[temp]=run.get(temp,0)+1

        return count            

        
