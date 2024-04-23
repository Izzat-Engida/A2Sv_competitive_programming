class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for num in range(left, right+1):
            if not any(a[0] <= num <= a[1] for a in ranges):
                return False
        return True
