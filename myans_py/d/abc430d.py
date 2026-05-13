from sortedcontainers import SortedList
from collections import defaultdict

n=int(input())
x=list(map(int, input().split()))

sl=SortedList()
sl.add(0)
d=defaultdict(int)

ans=0
for i in range(n):
    sl.add(x[i])
    idx=sl.index(x[i])
    
    # SLの前後を修正
    for j in [idx-1,idx,idx+1]:
        if 0<=j<len(sl):
            ans-=d[sl[j]]
            
            dist=10**18
            if j>0:
                dist=min(dist,sl[j]-sl[j-1])
            if j<len(sl)-1:
                dist=min(dist,sl[j+1]-sl[j])
            
            d[sl[j]]=dist
            ans+=dist
    
    print(ans)