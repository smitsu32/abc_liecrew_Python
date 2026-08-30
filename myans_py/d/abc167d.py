from math import log2

n,k=map(int, input().split())
a=list(map(int, input().split()))

# ダブリング:2進数の複数次元配列 [i][j]:jから2^i回移動
log=int(log2(k))+1
dub=[[0]*n for _ in range(log)]
for i in range(n):
    dub[0][i]=a[i]-1 #1回移動

for i in range(1,log):
    for j in range(n):
        dub[i][j]=dub[i-1][dub[i-1][j]] #2^j回移動を更新

ans=0
for i in range(log):
    if 1&k>>i: #kのbitが立っているところを追う
        ans=dub[i][ans]
print(ans+1) #1-indexed