class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        answer=[]
        def do(arr):
            i=0
            while i<len(arr):
                c=arr[i]-1
                if 0<=c<len(arr) and arr[c]!=arr[i]:
                    arr[i],arr[c]=arr[c],arr[i]
                else:
                    i+=1 
            return arr           
        nums=do(nums)

        for i in range(len(nums)):
            if i+1!=nums[i]:
                answer.append(i+1)
        return answer         
