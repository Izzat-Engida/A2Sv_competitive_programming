class Solution:
    def find132pattern(self, nums):
        n = len(nums)
        candidate_k = float('-inf')
        stack = []

        for i in range(n - 1, -1, -1):
            if nums[i] < candidate_k:
                return True
            else:
                while stack and stack[-1] < nums[i]:
                    candidate_k = stack[-1]
                    stack.pop()

            stack.append(nums[i])

        return False
