from heapq import heappop,heappush

n,m,y=map(int, input().split())
g=[[] for i in range(n+1)] # 0はワープ時の超頂点
for i in range(m):
    u,v,t=map(int, input().split())
    g[u].append((v,t))
    g[v].append((u,t))

x=list(map(int, input().split()))
for i in range(1,n+1):
    g[i].append((0,x[i-1]+y)) #ワープ中:x[i]+y
    g[0].append((i,x[i-1])) # ワープ後:x[j]

dist=[10**18]*(n+1)
dist[1]=0
hq=[(0,1)] #(距離,頂点)

while hq:
    d,u=heappop(hq)
    if d>dist[u]:
        continue
    
    for v,dd in g[u]:
        nd=d+dd
        if nd<dist[v]:
            heappush(hq,(nd,v))
            dist[v]=nd

print(*dist[2:])