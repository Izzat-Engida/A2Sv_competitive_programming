n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr, reverse=True) 
temp=[]
for i in arr:
    if i not in temp:
        temp.append(i)
 
print(temp[1])
