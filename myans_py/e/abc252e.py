# ダイクストラ法
from heapq import heappop,heappush,heapify

n,m=map(int, input().split())
g=[[] for i in range(n)]
for i in range(m):
    a,b,c=map(int, input().split())
    g[a-1].append([b-1,c,i]) # (v,cost,road_number)
    g[b-1].append([a-1,c,i])

dist=[10**18]*n # max=10**9 * 2*10**5
dist[0]=0

ans=[]
h=[(0,0,-1)] # (dist,u,road_number)

while h:
    d,u,idx=heappop(h)
    
    if d>dist[u]: continue #距離が長ければ使用しない
    
    if idx!=-1: #すでに更新済みのとき答え（dist昇順に探索するから）
        ans.append(idx)
    
    for v,c,nidx in g[u]: #接続辺を順番に探索
        if dist[v]>d+c:
            dist[v]=d+c
            heappush(h, (dist[v],v,nidx))

for i in ans:
    print(i+1,end=' ')