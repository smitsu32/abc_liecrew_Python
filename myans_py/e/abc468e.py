n=int(input())
a=list(map(int, input().split()))
MOD=998244353
# b:aの累積和
b,now=[0],0
for i in range(n):
    now=(now+a[i])%MOD
    b.append(now)

# h:sum(1/i)
h,now=[0],0
for i in range(1,1+n):
    now=(now+pow(i,MOD-2,MOD))%MOD
    h.append(now)

# 解法1の4行目の第一項、第二項(https://atcoder.jp/contests/abc468/editorial/23476)
# 最後の変形は理解をあきらめた
ans1,ans2=0,0
for r in range(1,n+1):
    ans1=(ans1+h[r]*b[r])%MOD
for l in range(1,n+1):
    ans2=(ans2+h[n-l+1]*b[l-1])%MOD

ans=(ans1-ans2)%MOD
print(ans)