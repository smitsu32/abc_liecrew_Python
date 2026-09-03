h,w=map(int, input().split())
s=[input() for i in range(h)]

def f(i,j,ni,nj):
    snuke='snukes'
    for k in range(5):
        if s[i][j]==snuke[k] and s[ni][nj]==snuke[k+1]:
            return True
    return False

visited=[[False]*w for i in range(h)]
visited[0][0]=True
d=[(0,0)]
while d:
    i,j=d.pop()
    for di,dj in [[1,0],[-1,0],[0,1],[0,-1]]:
        ni,nj=i+di,j+dj
        if 0<=ni<h and 0<=nj<w and f(i,j,ni,nj) and not visited[ni][nj]:
            visited[ni][nj]=True
            d.append((ni,nj))

print('Yes' if visited[-1][-1] else 'No')