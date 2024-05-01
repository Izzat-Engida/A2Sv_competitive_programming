class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        answer=[]
        i=0
        j=0
        while i<len(firstList) and j<len(secondList):
            s1,e1=firstList[i]
            s2,e2=secondList[j]
            if e1>=s2 and e2>=s1:
                i1=max(s1,s2)
                i2=min(e1,e2)
                answer.append([i1,i2])
            if e1<e2:
                i+=1
            else:
                j+=1
        return answer                    
        
