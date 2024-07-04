class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a=max(nums)
        b=min(nums)

        answer=self.f(a,b)
        return answer
    def f(self,a,b):
        if b==0:
            return a
        else:
            return self.f(b,a%b)       
        
