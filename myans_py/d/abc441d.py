n,m,l,s,t=map(int, input().split())

g=[[] for i in range(n)]
for i in range(m):
    u,v,c=map(int, input().split())
    g[u-1].append((v-1,c))

# DFS
d=[(0,0,0)] # (now_idx, cnt, cost)
# visited=[False]*n # 重複ありのため不要 

ans=set()
while d:
    now,cnt,cost=d.pop()
    
    if cnt==l:
        if s<=cost<=t:
            ans.add(now+1)
        continue
    
    if cnt<l:
        for nv,ncost in g[now]:
            if cost+ncost<=t:
                d.append((nv,cnt+1,cost+ncost))

print(*sorted(list(ans)))