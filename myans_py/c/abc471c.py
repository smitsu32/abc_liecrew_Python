from sortedcontainers import SortedList

n=int(input())
a=list(map(int, input().split()))

sl=SortedList(a)
ans,now=0,0
for _ in range(n):
    i=sl.bisect_left(now)
    if i==0:
        nn=sl[0]
    elif i==len(sl):
        nn=sl[-1]
    else:
        l,r=sl[i-1],sl[i]
        if abs(l-now)<=abs(r-now):
            nn=l
        else:
            nn=r
    
    sl.remove(nn)
    ans+=abs(now-nn)
    now=nn

print(ans)