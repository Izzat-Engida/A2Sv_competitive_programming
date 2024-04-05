class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i=0
        l=len(people)
        j=l-1
        count=0
        while i<=j:
            if people[j]+people[i]<=limit:
                count+=1
                i+=1
                j-=1
            else:
                count+=1
                j-=1               
        return count        
                    
