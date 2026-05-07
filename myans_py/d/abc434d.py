n=int(input())

# 累積和
def prefix(a):
    for i in range(1,2001):
        for j in range(1,2001):
            a[i][j]+=a[i-1][j]+a[i][j-1]-a[i-1][j-1]
    return a

# a:2次元いもす法→累積和
a=[[0]*2002 for _ in range(2002)]
u,d,l,r=[0]*n,[0]*n,[0]*n,[0]*n
for i in range(n):
    u[i],d[i],l[i],r[i]=map(int, input().split())
    a[u[i]][l[i]]+=1
    a[u[i]][r[i]+1]-=1
    a[d[i]+1][l[i]]-=1
    a[d[i]+1][r[i]+1]+=1

a=prefix(a)

# b:雲一つのみ
cnt=0 # 雲0個
b=[[0]*2002 for _ in range(2002)]
for i in range(1,2001):
    for j in range(1,2001):
        if a[i][j]==0:
            cnt+=1
        elif a[i][j]==1:
            b[i][j]=1

b=prefix(b)
# 雲iを除いたとき0個になる範囲を出力
for i in range(n):
    ans=cnt
    ans+=b[d[i]][r[i]]-b[d[i]][l[i]-1]-b[u[i]-1][r[i]]+b[u[i]-1][l[i]-1]
    print(ans)