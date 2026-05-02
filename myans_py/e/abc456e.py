for i in range(int(input())):
    n,m=map(int, input().split())
    g=[[i] for i in range(n)] #自分OK
    for i in range(m):
        u,v=map(int, input().split())
        g[u-1].append(v-1)
        g[v-1].append(u-1)
    w=int(input())
    s=[input() for i in range(n)]
    
    # i=day*N+cityとして1次元化 (0~N*W)
    G=[[] for i in range(n*w)]
    for i in range(n): # city
        for j in range(w): # day
            if s[i][j]=='x': continue
            
            for ni in g[i]:
                nj=(j+1)%w
                if s[ni][(j+1)%w]=='o':
                    G[j*n+i].append(nj*n+ni)
    
    visited=[False]*(n*w)
    end=[False]*(n*w) 
    f=False
    
    for i in range(n*w): # 各曜日、場所スタートを試す
        if visited[i] or s[i%n][i//n]=='x': # (city,day)
            continue
        
        l=[(i,0)] # now,next(G[now]のidx)
        while l:
            ni,idx=l[-1]
            if idx==0:
                visited[ni]=True
            
            if idx>=len(G[ni]): # G[i]探索完了
                end[ni]=True
                l.pop()
            else:
                nj=G[ni][idx]
                l[-1]=(ni,idx+1) # G_idx更新
                if not visited[nj]: # 次の点更新
                    l.append((nj,0))
                elif not end[nj]: # 1回通ったときYes
                    f=True
                    break
        if f:
            break
    
    print('Yes' if f else 'No')