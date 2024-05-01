size1, size2 = map(int, input().split())
 
   
arr1 = list(map(int, input().split()))
 

arr2 = list(map(int, input().split()))
 
i, j, k = 0, 0, 0
 
    
arr3 = [0] * (size1 + size2)
arr4 = [0] * size2
 
 
while i < size1 or j < size2:
    if j == size2 or (i < size1 and arr1[i] < arr2[j]):
        arr3[k] = arr1[i]
        i += 1
    else:
        arr4[j] = i
        arr3[k] = arr2[j]
        j += 1
    k += 1
print(*arr4)    
