from bisect import bisect_left,bisect_right

n,m=map(int, input().split())
a=list(map(int, input().split()))

# 10**i*a[i]
l=[[] for i in range(11)]
for i in range(11):
    for j in range(n):
        l[i].append(a[j]*10**i%m)
    l[i].sort() # 桁ごとのあまり

ans=0
# a[i]*10^(len(a[j]))+a[j] ≡ 0 (mod M)
# a[i]*10^(len(a[j])) ≡ -a[j] (mod M)
for j in range(n):
    d=len(str(a[j]))
    i=-a[j]%m
    ans+=bisect_right(l[d],i)-bisect_left(l[d],i)

print(ans)