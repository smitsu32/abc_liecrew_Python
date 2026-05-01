n=int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
c=list(map(int, input().split()))
INF=10**18

# i番目が[頭,銅,尾]のときの最大値
dp=[[0,-INF,-INF] for i in range(n)]
dp[0][0]=a[0]

for i in range(1,n):
    dp[i][2]=max(dp[i-1][1],dp[i-1][2])+c[i] # 尾まで到達可能ならmax(胴)+尾
    dp[i][1]=max(dp[i-1][0],dp[i-1][1])+b[i]
    dp[i][0]=dp[i-1][0]+a[i]

print(dp[-1][2])