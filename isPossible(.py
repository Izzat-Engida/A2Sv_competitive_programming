class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        subsequences = defaultdict(list)
        for num in nums:
            if subsequences[num - 1]:
                prev_length = heappop(subsequences[num - 1])
                heappush(subsequences[num], prev_length + 1)
            else:
                heappush(subsequences[num], 1)
        for lengths in subsequences.values():
            if lengths and lengths[0] < 3:
                return False
        return True
