class Solution:
    def largestNumber(self, nums: List[int]) -> str:
    
        nums=sorted(nums,key=lambda x:str(x)*9,reverse=True )
        ans=''.join(map(str,nums))
        return '0' if ans[0]=='0' else ans
       
        
        
