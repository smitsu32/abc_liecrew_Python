x,y,z=map(int, input().split())
s=input()
n=len(s)

dp=[[10**18]*2 for i in range(n+1)] #i文字目でCaps(On/off)時の到達時間
dp[0][0],dp[0][1]=0,z
for i in range(n):
    if s[i]=='a':
        dp[i+1][0]=min(dp[i][0]+x,dp[i][1]+z+x)
        dp[i+1][1]=min(dp[i][0]+z+y,dp[i][1]+y)
    else:
        dp[i+1][0]=min(dp[i][0]+y,dp[i][1]+z+y)
        dp[i+1][1]=min(dp[i][0]+z+x,dp[i][1]+x)

print(min(dp[-1]))