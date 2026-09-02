n,m=map(int, input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))

g=[[] for i in range(n)]
for i in range(m):
    g[a[i]-1].append(b[i]-1)
    g[b[i]-1].append(a[i]-1)

x=[-1]*n
f=True
for i in range(n): #全点からDFS
    if x[i]!=-1:
        continue
    x[i]=0
    l=[[i,0]] # 点、色
    while l:
        u,c=l.pop()
        for v in g[u]:
            if x[v]==-1:
                x[v]=c^1
                l.append([v,c^1])
            if x[v]==c:
                f=False
                break

print('Yes' if f else 'No')