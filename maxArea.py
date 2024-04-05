class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        area=0
        while i<j:
            temp=(j-i) * min(height[i],height[j])
            area=max(area,temp)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return area            
        
