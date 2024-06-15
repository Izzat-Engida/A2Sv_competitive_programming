class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sums = 0
        run = {0:1}
        
        for num in nums:
            sums += num
            x=sums-k
            if x in run:
                count+=run.get(sums-k,0)
            run[sums]=run.get(sums,0)+1    
            
        return count
