from bisect import bisect_left,bisect_right
MOD=998244353

n,m=map(int, input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
b.sort()

# 累積和
bb=[0]
for i in range(m):
    bb.append(bb[-1]+b[i])

ans=0
for i in range(n):
    c=bisect_left(b,a[i]) # 絶対値でわける
    ans+=c*a[i]-(bb[c]-bb[0])
    ans+=(bb[-1]-bb[c])-a[i]*(m-c)
    ans%=MOD

print(ans)