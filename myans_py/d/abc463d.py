from bisect import bisect_left,bisect_right

n,k=map(int, input().split())
lr=[list(map(int, input().split())) for i in range(n)]
lr.sort(key=lambda x:x[1])

# d:間隔 で二分探索
def c(d):
    rmax,cnt=-10**18,0
    for l,r in lr:
        if l-rmax>=d:
            rmax=r
            cnt+=1
    return cnt>=k

ok,ng=0,10**18
while abs(ok-ng)>1:
    mid=(ok+ng)//2
    if c(mid):
        ok=mid
    else:
        ng=mid

print(ok if ok>0 else -1)