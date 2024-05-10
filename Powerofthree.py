class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<1:
            return False
        elif n==1:
            return True

        else:
            return self.isPowerOfThree(n/3 if n%3==0 else 0)
