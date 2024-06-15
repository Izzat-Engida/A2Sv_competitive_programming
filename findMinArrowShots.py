class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        tempx,tempy=points[0]
        mcount=0
        print(points)
        for i in range(1,len(points)):
            x,y=points[i]
            if tempx<=x<=tempy:
                tempx=max(tempx,x)
                tempy=min(y,tempy)
            else:
                mcount+=1
                tempx,tempy=x,y
        return mcount+1           

        
