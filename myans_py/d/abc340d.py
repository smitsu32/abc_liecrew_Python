from heapq import heappop,heappush

n=int(input())
a,b,x=[0]*(n-1),[0]*(n-1),[0]*(n-1)
for i in range(n-1):
    a[i],b[i],x[i]=map(int, input().split())

dist=[10**18]*n
dist[0]=0

# ダイクストラ法
h=[(0,0)] #(距離、点)
while h:
    d,u=heappop(h)
    
    if u==n-1: #ゴール
        break
    if d!=dist[u]: #無向グラフ逆流
        continue
    
    nd=d+a[u] #i->i+1
    if nd<dist[u+1]:
        dist[u+1]=nd
        heappush(h,(nd,u+1))
    nd=d+b[u] #i->x[i]
    if nd<dist[x[u]-1]:
        dist[x[u]-1]=nd
        heappush(h,(nd,x[u]-1))
print(dist[-1])