class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq={}
        for num in nums1:
            if num not in freq:
                freq[num]=0
            freq[num]+=1
        intersect=[]
        for num in nums2:
            if num in freq and freq[num]>0:
                intersect.append(num)
                freq[num]-=1
        return intersect            
