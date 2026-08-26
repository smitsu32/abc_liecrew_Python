from collections import deque

for _ in range(int(input())):
    n,m=map(int, input().split())
    g=[[] for _ in range(n)]
    for _ in range(m):
        a,b=map(int, input().split())
        g[a-1].append(b-1); g[b-1].append(a-1)
    
    c,p=[-1]*n,[-1]*n # 色、親
    c[0]=0
    
    d=deque([0])
    f=True
    while d:
        u=d.popleft()
        for v in g[u]:
            if c[v]==-1:
                c[v]=c[u]^1 # 0,1,0,...と交互に塗る（奇数長判別）
                p[v]=u
                d.append(v)
            else:
                if c[u]!=c[v]: # 戻る方向をスキップ
                    continue
                
                r,e=[],[] #ループ始点と終点から根をルート探索
                x,y=u,v
                while x!=-1:
                    r.append(x)
                    x=p[x]
                while y!=-1:
                    e.append(y)
                    y=p[y]
                while r[-1]==e[-1]: # 根から閉路外削除
                    w=r.pop()
                    e.pop()
                
                ans=r+[w]+e[::-1] # 閉路外->r->w->e(末端から)
                
                print(len(ans))
                for i in ans:
                    print(i+1,end=' ')
                f=False
                break
        if not f:
            break
    if f:
        print(-1)