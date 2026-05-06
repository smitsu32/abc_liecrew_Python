from collections import deque

h,w=map(int, input().split())
s=[input() for i in range(h)]

warp=[[] for i in range(26)] #ワープます
for i in range(h):
    for j in range(w):
        if 'a'<=s[i][j]<='z':
            warp[ord(s[i][j])-ord('a')].append((i,j))

visited=[[-1]*w for i in range(h)]
visited[0][0]=0

fwarp=[False]*26 # 既に探索したワープか

d=deque()
d.append((0,0))

while d:
    i,j=d.popleft()
    if (i,j)==(h-1,w-1):
        break
    
    for di,dj in [[1,0],[-1,0],[0,1],[0,-1]]:
        ni,nj=i+di,j+dj
        if 0<=ni<h and 0<=nj<w and s[ni][nj]!='#' and visited[ni][nj]==-1:
            visited[ni][nj]=visited[i][j]+1
            d.append((ni,nj))
    
    if 'a'<=s[i][j]<='z': #　ワープ
        idx=ord(s[i][j])-ord('a')
        
        if not fwarp[idx]:
            fwarp[idx]=True
            for ni,nj in warp[idx]:
                if visited[ni][nj]!=-1: #すでに到達済みのとき(同時到達)
                    continue
                
                visited[ni][nj]=visited[i][j]+1
                d.append((ni,nj))

print(visited[-1][-1])