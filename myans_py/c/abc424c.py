n=int(input())
g=[[] for i in range(n+1)] #0:超頂点
for i in range(n):
    a,b=map(int, input().split())
    g[a].append(i+1)
    if a!=b:
        g[b].append(i+1)

visited=[False]*(n+1)
d=list(g[0])
while d:
    dd=d.pop()
    visited[dd]=True #g[0]のため
    for nd in g[dd]:
        if not visited[nd]:
            visited[nd]=True
            d.append(nd)

ans=0
for i in visited:
    if i==True: ans+=1
print(ans)