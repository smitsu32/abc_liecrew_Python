from collections import deque

n,m=map(int, input().split())
g=[[] for i in range(n)]
for i in range(m):
    ai,bi=map(int, input().split())
    g[ai-1].append(bi-1)

cnt=1
d=deque([0])
visited=[False]*n
visited[0]=True
while d:
    a=d.popleft()
    for b in g[a]:
        if not visited[b]:
            cnt+=1
            d.append(b)
            visited[b]=True
print(cnt)