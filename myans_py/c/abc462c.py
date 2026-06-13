n=int(input())
g=[list(map(int, input().split())) for i in range(n)]
g.sort()

ans,miny=0,n+1
for i in range(n):
    x,y=g[i]
    if y<miny:
        ans+=1
    miny=min(y,miny)

print(ans)