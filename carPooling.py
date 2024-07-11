class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trip_length=[0]*1001
        for trip in trips:
            trip_length[trip[1]]+=trip[0]
            trip_length[trip[2]]-=trip[0]
        capa=0    
        for trip in trip_length:
            capa+=trip
            if capa>capacity:
                return False
        return True        
