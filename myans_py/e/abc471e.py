# AI解をrefine
n,k=map(int, input().split())
a=list(map(int, input().split()))
MOD=998244353

# 2乗項と1乗項の登場回数から
# (n-1,k-1)sum(Ai^2) + (n-2,k-2)sum(sum(AiAj)) (i!=j)
# s1=sum(Ai), s2=sum(sum((AiAj))とすると
# (上式)=(n-1,k-1)s1^2 + (n-2,k-2)s2^2
s1=sum(a)%MOD
s2=sum(i*i for i in a)%MOD

# nCk=n!/(k!(n-k)!)より階乗とその逆元を求める
now=1
f=[now]
for i in range(1,n+1):
    now=(now*i)%MOD
    f.append(now)
now=pow(f[-1],MOD-2,MOD)
finv=[now]
for i in range(n,0,-1): #inv[i-1]=inv[i]*iよりi->i-1(逆順)
    now=(now*i)%MOD
    finv.append(now)
finv=finv[::-1]

ans1,ans2=0,0
if k-1>=0:
    ans1=f[n-1]*finv[k-1]*finv[n-k]%MOD
if k-2>=0:
    ans2=f[n-2]*finv[k-2]*finv[n-k]%MOD

print((ans1*s2+ans2*(s1**2-s2))%MOD)