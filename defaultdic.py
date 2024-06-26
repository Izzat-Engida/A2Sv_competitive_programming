# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict


n, m = map(int, input().split())
d = defaultdict(list)
    
for i in range(1, n + 1):
    d[input()].append(str(i))
        
for _ in range(m):
    print(' '.join(d[input()]) or -1)


