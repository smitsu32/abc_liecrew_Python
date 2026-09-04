n=int(input())
ab=[list(map(int, input().split())) for i in range(n)]
MOD=998244353

dp=[[0]*2 for _ in range(n)]
dp[0][0],dp[0][1]=1,1
for i in range(n-1):
    for j in range(2): #前
        for k in range(2): #次
            if ab[i][j]!=ab[i+1][k]: #一致しなかったら足す
                dp[i+1][k]=(dp[i+1][k]+dp[i][j])%MOD
print(sum(dp[-1])%MOD)