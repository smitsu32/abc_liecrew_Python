n,m=map(int, input().split())
con=[0]*n #各点の連結数
g=[[] for i in range(n)]
for i in range(m):
    a,b,c,d=input().split()
    con[int(a)-1]+=1; con[int(c)-1]+=1
    g[int(a)-1].append(int(c)-1); g[int(c)-1].append(int(a)-1)

visited=[False]*n
x,y=0,0
for i in range(n):
    if visited[i]:
        continue
    l=[i]
    visited[i]=True
    f=True
    while l:
        u=l.pop()
        if con[u]!=2:
            f=False
        for v in g[u]:
            if not visited[v]:
                visited[v]=True
                l.append(v)
    if f:
        x+=1
    else:
        y+=1
print(x,y)