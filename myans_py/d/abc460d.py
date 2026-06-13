from collections import deque

h,w=map(int, input().split())
s=[list(input()) for _ in range(h)]
vec=[[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]

ns=[['.']*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j]=='#':
            for di,dj in vec:
                ni,nj=i+di,j+dj
                if 0<=ni<h and 0<=nj<w and s[ni][nj]=='.':
                    ns[ni][nj]='#'

d=[[-1]*w for _ in range(h)]
q=deque()
for i in range(h):
    for j in range(w):
        if ns[i][j]=='#':
            d[i][j]=0
            q.append((i,j))

while q:
    ii,jj=q.popleft()
    for di,dj in vec:
        ni,nj=ii+di,jj+dj
        if 0<=ni<h and 0<=nj<w and d[ni][nj]==-1:
            d[ni][nj]=d[ii][jj]+1
            q.append((ni,nj))

for i in range(h):
    for j in range(w):
        if d[i][j]%2==0 or d[i][j]<0:
            ns[i][j]='.'
        else:
            ns[i][j]='#'

for i in range(h):
    print(''.join(ns[i]))