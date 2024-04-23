class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        max_val = max(heights)
        count = [0] * (max_val + 1)
        output = [0] * len(heights)

        for num in heights:
            count[num] += 1

        for i in range(1, len(count)):
            count[i] += count[i - 1]
        for i in range(len(heights) - 1, -1, -1):
            output[count[heights[i]] - 1] = heights[i]
            count[heights[i]] -= 1

        return output    

    
