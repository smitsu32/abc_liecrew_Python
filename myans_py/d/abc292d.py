from atcoder.dsu import DSU

n,m=map(int, input().split())
d=DSU(n)
uv=[]
for i in range(m):
    u,v=map(int, input().split())
    d.merge(u-1,v-1)
    uv.append((u-1,v-1))

g=[0]*n
for u,_ in uv:
    g[d.leader(u)]+=1 #リーダーに辺数を集約

for l in d.groups():
    if len(l)!=g[d.leader(l[0])]: #点!=辺
        print('No')
        exit()
print('Yes')