from collections import deque

n1,n2,m=map(int, input().split())
g=[[] for i in range(n1+n2)]
for i in range(m):
    a,b=map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

def f(sta):
    dis=[-1]*(n1+n2)
    dis[sta]=0
    d=deque([sta])
    while d:
        u=d.popleft()
        for v in g[u]:
            if dis[v]!=-1:
                continue
            dis[v]=dis[u]+1
            d.append(v)
    return max(dis)

print(f(0)+f(n1+n2-1)+1)