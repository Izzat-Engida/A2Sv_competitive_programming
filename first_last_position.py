class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        lefti = self.binary(nums, target, True)
        if lefti == len(nums) or nums[lefti] != target:
            return result
        result[0] = lefti
        result[1] = self.binary(nums, target, False) - 1
        return result

    def binary(self, nums, target, findLeft):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target or (findLeft and nums[mid] == target):
                right = mid - 1
            else:
                left = mid + 1
        return left if findLeft else right + 1
