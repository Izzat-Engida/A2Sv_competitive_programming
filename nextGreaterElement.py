class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        temp = []
        ans = -1
        for a in nums1:
            ans = -1
            for i in range(len(nums2)):
                if a == nums2[i]:
                    for k in range(i, len(nums2)):
                        if a < nums2[k]:
                            ans = nums2[k]
                            break
                    temp.append(ans)
                    break
        return temp
