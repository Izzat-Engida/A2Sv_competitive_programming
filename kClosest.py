class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans1=[]
        for p in points:
            d=sqrt((p[0]*p[0])+(p[1])*(p[1]))
            p.append(d)
        points.sort(key=lambda p: p[2])    

        return [p[:2]for p in points[:k]]              


        
