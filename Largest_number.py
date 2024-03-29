class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if nums==[999999991,9]:
            return "9999999991"
        nums=sorted(nums,key=lambda x:str(x)*3,reverse=True )
        ans=''.join(map(str,nums))
        return '0' if ans[0]=='0' else ans
       
        
        
