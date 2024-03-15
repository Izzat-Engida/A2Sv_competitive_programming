class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(n,( 2 * n)+1):
            if i%n==0 and i % 2 == 0:
                return i
        return n  

