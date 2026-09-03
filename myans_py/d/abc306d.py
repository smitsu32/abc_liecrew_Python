n=int(input())
dp=[[-10**18]*2 for i in range(n+1)]
dp[0][0]=0

for i in range(n):
    x,y=map(int, input().split())
    if x==0: #毒じゃない:戻るか食べない
        dp[i+1][0]=max(dp[i][0],max(dp[i][0],dp[i][1])+y)
        dp[i+1][1]=dp[i][1]
    else: #毒:食べないかお腹壊す
        dp[i+1][0]=dp[i][0]
        dp[i+1][1]=max(dp[i][1],dp[i][0]+y)
print(max(dp[-1]))