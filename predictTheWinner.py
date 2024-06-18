class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        
        def dothejob(i, j):
            if i == j:
                return nums[i]
            if dp[i][j] > 0:
                return dp[i][j]
            dp[i][j] = max(nums[i] - dothejob(i+1, j), nums[j] - dothejob(i, j-1))
            return dp[i][j]
        
        return dothejob(0, n-1) >= 0
