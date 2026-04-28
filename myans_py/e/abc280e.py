n,p=map(int, input().split())
MOD=998244353
# dp[i]:体力iから0になる攻撃回数の期待値
# (体力i+2からiになる)+(体力i+1からiになる)+1回攻撃
# dp[i] = 0.01p*dp[i-2] + (1-0.01)p*dp[i-1]+1

dp=[0]*(n+1)
div=pow(100,-1,MOD) #誤差防止で逆元
for i in range(1,n+1):
    if i==1:
        dp[i]=1
    else:
        dp[i]=dp[i-2]*(p*div)%MOD + dp[i-1]*((100-p)*div)%MOD + 1
        dp[i]%=MOD

print(dp[n])