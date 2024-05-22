class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        j=len(cardPoints)
        lsum=sum(cardPoints[:k])
        maxsum=lsum
        rsum=0
        for i in range(k):
            lsum-=cardPoints[k-i-1]
            rsum+=cardPoints[j-i-1]
            maxsum=max(maxsum,lsum+rsum)
        return maxsum    


                 
