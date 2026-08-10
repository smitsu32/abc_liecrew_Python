n=int(input())
INF=10**18

#同時に動けるから一番遠いのを独立に考える
mxx,mnx,mxy,mny=-INF,INF,-INF,INF
for i in range(n):
    x,y=map(int, input().split())
    mxx=max(mxx,x)
    mnx=min(mnx,x)
    mxy=max(mxy,y)
    mny=min(mny,y)

print(max((mxx-mnx+1)//2,(mxy-mny+1)//2))