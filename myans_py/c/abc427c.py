n,m=map(int, input().split())
g=[[] for _ in range(n)]
for i in range(m):
    u,v=map(int, input().split())
    g[u-1].append(v-1); g[v-1].append(u-1)

# 切る本数
ans=m
# 最初に0,1に分け、削除辺数を記録
for bit in range(2**n):
    d=[False]*n
    for i in range(n):
        if 1&(bit>>i):
            d[i]=True
    
    # 切る辺数
    crr=0
    for i in range(n):
        for j in g[i]:
            if i<j and d[i]==d[j]: # 重複防止
                crr+=1
    ans=min(crr,ans)

print(ans)