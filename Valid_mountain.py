class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        ma=max(arr)
        if arr[len(arr)-1]==ma or arr[0]==ma:
            return False
        i=0
        turn=False
        while i<len(arr)-1:
            if arr[i]==ma:
                turn=True
            if not turn:
                if arr[i]>=arr[i+1]:
                    return False
            if turn:
                if arr[i]<=arr[i+1]:
                    return False
            i+=1
        return True                    




        
