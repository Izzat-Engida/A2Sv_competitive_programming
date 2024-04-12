class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def check(arr):
            for i in range(1,len(arr)):
                if arr[i-1]>arr[i]:
                    return False
            return True
        j=len(arr)
        ans=[]
        while not check(arr):
            maxi=0
            maxv=arr[0]
            for i in range(1,j):
                if maxv<arr[i]:
                    maxv=arr[i]
                    maxi=i
            arr[:maxi + 1]=reversed(arr[:maxi+1])
            ans.append(maxi+1)
            arr[:j]=reversed(arr[:j])
            ans.append(j)
            j-=1
        return ans                        
