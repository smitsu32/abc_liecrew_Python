n,m=map(int, input().split())

# 逆向きにして格納
g=[[] for i in range(n)]
for i in range(m):
    x,y=map(int, input().split())
    g[y-1].append(x-1)

ok=[False]*n #黒点から到達可能か
for i in range(int(input())):
    q=list(map(int, input().split()))
    v=q[1]-1
    if q[0]==1:
        if not ok[v]:
            ok[v]=True
            d=[v]
            while d:
                u=d.pop()
                for nv in g[u]:
                    if not ok[nv]:
                        ok[nv]=True
                        d.append(nv)
    else:
        if ok[v]:
            print('Yes')
        else:
            print('No')