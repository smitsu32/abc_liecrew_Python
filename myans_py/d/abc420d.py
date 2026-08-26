from collections import deque

h,w=map(int, input().split())
a=[input() for _ in range(h)]
INF=10**18

for i in range(h):
    for j in range(w):
        if a[i][j]=='S':
            s=(i,j)
        if a[i][j]=='G':
            g=(i,j)

dist=[[[INF]*w for _ in range(h)] for _ in range(2)] # (flag,i,j)
dist[0][s[0]][s[1]]=0
d=deque([(s[0],s[1],0)])
while d:
    i,j,f=d.popleft()
    for di,dj in [[1,0],[-1,0],[0,1],[0,-1]]:
        ni,nj=i+di,j+dj
        if 0<=ni<h and 0<=nj<w and a[ni][nj]!='#':
            if (f==0 and a[ni][nj]=='x') or (f==1 and a[ni][nj]=='o'):
                continue
            
            nf=f^(a[ni][nj]=='?')
            if dist[nf][ni][nj]!=INF:
                continue
            dist[nf][ni][nj]=dist[f][i][j]+1
            d.append((ni,nj,nf))

ans=min(dist[0][g[0]][g[1]],dist[1][g[0]][g[1]])
print(ans if ans!=INF else -1)