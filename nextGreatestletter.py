class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i=0
        j=len(letters)-1
        while i<=j:
            mid=(i+j)//2
            if letters[mid]<=target:
                i=mid+1
            else:
                j=mid-1
        return letters[i%len(letters)]
