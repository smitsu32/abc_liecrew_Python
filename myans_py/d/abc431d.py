n=int(input())

# 体が重さjのときの最大幸せ度
dp=[0]
for i in range(n):
    w,h,b=map(int, input().split())
    
    m=len(dp)
    ndp=[0]*(m+w)
    for j in range(m):
        #頭
        ndp[j]=max(ndp[j],dp[j]+h)
        #体
        ndp[j+w]=max(ndp[j+w],dp[j]+b)
    dp=ndp[:]

#体の重さが全体の半分以上
ans=max(dp[len(dp)//2:])
print(ans)