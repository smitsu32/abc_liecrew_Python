from collections import deque

h,w,k=map(int, input().split())
s=[input() for i in range(h)]

fh,fw=[False]*h,[False]*w
for i in range(h):
    for j in range(w):
        if s[i][j]=='#':
            fh[i],fw[j]=True,True

d=deque()
sf=[[10**18]*w for i in range(h)]
for i in range(h):
    for j in range(w):
        if not fh[i] and not fw[j]:
            d.append((i,j))
            sf[i][j]=0

vec=[[1,0],[-1,0],[0,1],[0,-1]]
while d:
    i,j=d.popleft()
    for di,dj in vec:
        ni,nj=i+di,j+dj
        if 0<=ni<h and 0<=nj<w and s[ni][nj]=='.' and sf[i][j]+1<sf[ni][nj]:
            sf[ni][nj]=sf[i][j]+1
            d.append((ni,nj))

ans=0
for i in range(h):
    for j in range(w):
        if sf[i][j]<=k:
            ans+=1
print(ans)