from collections import deque

h,w=map(int, input().split())
s=[input() for i in range(h)]

used=[[False]*w for i in range(h)]
vec=[[1,0],[-1,0],[0,1],[0,-1]]

def bfs(x,y):
    f=True
    q=deque()
    q.append((x,y))
    while q:
        i,j=q.popleft()
        if i in (0,h-1) or j in (0,w-1):
            f=False
        
        for di,dj in vec:
            ni,nj=i+di,j+dj
            if 0<=ni<h and 0<=nj<w and s[ni][nj]=='.' and not used[ni][nj]:
                q.append((ni,nj))
                used[ni][nj]=True
    return f

ans=0
for i in range(h):
    for j in range(w):
        if s[i][j]=='.' and not used[i][j]:
            if bfs(i,j):
                ans+=1

print(ans)