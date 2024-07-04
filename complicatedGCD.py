def solve(a,b):
    if b==a:
        return a
    else:
        return 1
a,b=map(int,input().split())
print(solve(a,b))
