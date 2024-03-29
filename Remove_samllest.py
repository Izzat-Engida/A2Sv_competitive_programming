t=int(input())
while t>0:
    n=int(input())
    arr = list(map(int, input().split()))
    i=0
    j=n-1
    while j!=i:
        if abs(arr[i]-arr[j])<=1:
            if arr[i]>arr[j]:
                del arr[j]
            elif arr[i]<arr[j]:
                del arr[i]
            else:
                del arr[j]       
        j-=1
    if len(arr)==1:
        print("YES")
    else:
        print("NO")        

    t-=1
