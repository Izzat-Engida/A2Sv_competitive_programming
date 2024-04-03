class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = nums.copy()
        ans = [0] * len(arr)
        arr.sort()
        k = 0
        for i in range(len(arr)):
            for j in range(len(arr)):
                if nums[i] == arr[j]:
                    ans[k] = j
                    k += 1
                    break
        return ans


        
