class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        count=0
        s=0
        for i in costs:
            if s+i<=coins:
                count+=1
                s+=i
            else:
                break
        return count                
