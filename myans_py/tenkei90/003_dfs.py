import sys
sys.setrecursionlimit(10**6)

n=int(input())
g=[[] for _ in range(n)]
for _ in range(n-1):
    ai,bi=map(int,input().split())
    ai-=1; bi-=1
    g[ai].append(bi)
    g[bi].append(ai)

#dfs
dis1=[-1]*n
dis1[0]=0
def dfs1(s):
    for v in g[s]:
        if dis1[v]==-1:
            dis1[v]=dis1[s]+1
            dfs1(v)

dfs1(0)
idx1=0
mx1=max(dis1)
for i in range(n):
    if dis1[i]==mx1:
        idx1=i
        break


dis2=[-1]*n
dis2[idx1]=0
def dfs2(s):
    for v in g[s]:
        if dis2[v]==-1:
            dis2[v]=dis2[s]+1
            dfs2(v)

dfs2(idx1)
mx2=max(dis2)
print(mx2+1)