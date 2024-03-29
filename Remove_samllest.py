    t=int(input())
    while t>0:
        n=int(input())
        arr = list(map(int, input().split()))
        arr.sort()
        for i in range(n-1):
            if abs(arr[i]-arr[i+1])>1:
                print("NO")
                break
        else:
            print("Yes")
     
        t-=1
