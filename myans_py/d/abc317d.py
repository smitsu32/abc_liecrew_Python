n=int(input())
x,y,z,w=[0]*n,[0]*n,[0]*n,[0]*n
for i in range(n):
    x[i],y[i],z[i]=map(int, input().split())
    if x[i]<y[i]:
        w[i]=(y[i]-x[i]+1)//2 #鞍替えに必要な人数

m=sum(z)
dp=[10**18]*(m+1) #i人獲得するための鞍替え人数
dp[0]=0
for i in range(n):
    for j in range(m,z[i]-1,-1): #同じ区が重複しないよう人数逆順
        dp[j]=min(dp[j],dp[j-z[i]]+w[i])

print(min(dp[(m+1)//2:]))