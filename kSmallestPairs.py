class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        ans = []  
        i, j = 0, 0
        v = set()
        v.add((i, j))
        heapq.heappush(heap, (nums1[0] + nums2[0], (i, j)))
        
        while k and heap:
            temp, (i, j) = heapq.heappop(heap)
            ans.append([nums1[i], nums2[j]])
            
            if i + 1 < len(nums1) and (i + 1, j) not in v:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], (i + 1, j)))
                v.add((i + 1, j))
                
            if j + 1 < len(nums2) and (i, j + 1) not in v:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], (i, j + 1)))
                v.add((i, j + 1))
                
            k -= 1
        
        return ans

