class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        for size in reversed(range(1, len(arr) + 1)):
            max_idx = arr.index(max(arr[:size]))
            arr[:max_idx + 1] = reversed(arr[:max_idx + 1])
            arr[:size] = reversed(arr[:size])
            ans.extend([max_idx + 1, size])
        return ans
