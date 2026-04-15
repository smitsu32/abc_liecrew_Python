# ref: https://atcoder.jp/contests/abc453/submissions/74966438
from collections import deque

H,W=map(int, input().split())
s=[input() for i in range(H)]

dh,dw,v=[-1,1,0,0],[0,0,-1,1],['U','D','L','R']
visited=[[[-1]*4 for i in range(W)]for i in range(H)] # [h][w][direction_idx]=before_dir_index

for i in range(H):
    for j in range(W):
        if s[i][j]=='S':
            sh,sw=i,j

d=deque() # (h,w,dir_idx)
g=-2 # t
for i in range(4):
    d.append((sh,sw,i))
    visited[sh][sw][i]=g

gf=None
while d:
    h,w,dir=d.popleft()
    if s[h][w]=='G':
        gf=(h,w,dir)
        break
    
    for ndir in range(4):    
        if s[h][w]=='o' and ndir!=dir:
            continue
        if s[h][w]=='x' and ndir==dir:
            continue
        
        nh,nw=h+dh[ndir],w+dw[ndir]
        if 0<=nh<H and 0<=nw<W and s[nh][nw]!='#' and visited[nh][nw][ndir]==-1:
            d.append((nh,nw,ndir))
            visited[nh][nw][ndir]=dir

if gf:
    ans=[]
    h,w,dir=gf
    while dir!=g:
        ans.append(v[dir])
        pdir=visited[h][w][dir]
        h-=dh[dir]
        w-=dw[dir]
        dir=pdir
    print('Yes')
    print(''.join(reversed(ans[:-1])))
else:
    print('No')