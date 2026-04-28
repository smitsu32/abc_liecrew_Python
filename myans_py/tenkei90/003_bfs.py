import sys
sys.setrecursionlimit(10**6)
from collections import deque

n=int(input())
g=[[] for _ in range(n)]
for _ in range(n-1):
    ai,bi=map(int,input().split())
    ai-=1; bi-=1
    g[ai].append(bi)
    g[bi].append(ai)

#bfs:0->最遠ノードi, i->最遠ノードまでの距離 + 1(追加分)
dis1=[-1]*n
dis1[0]=0

q=deque()
q.append(0)
while q:
    s=q.popleft()
    for v in g[s]:
        if dis1[v]==-1:
            dis1[v]=dis1[s]+1
            q.append(v)

idx1=0
mx1=max(dis1)
for i in range(n):
    if dis1[i]==mx1:
        idx1=i
        break


dis2=[-1]*n
dis2[idx1]=0

q=deque()
q.append(idx1)
while q:
    s=q.popleft()
    for v in g[s]:
        if dis2[v]==-1:
            dis2[v]=dis2[s]+1
            q.append(v)

mx2=max(dis2)
print(mx2+1)