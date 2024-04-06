class Solution: 
    def select(self, arr, i):
        
        # code here 
        small=i-1
        for j in range(i,len(arr)):
            if arr[small]> arr[j]:
                small=j
        return small        
            
    
    def selectionSort(self, arr,n):
        
        #code here
        for i in range(n):
            small=self.select(arr,i+1)
            arr[i],arr[small]=arr[small],arr[i]
        return arr    
