from bisect import bisect_left,bisect_right

n=int(input())
a=list(map(int, input().split()))

f=[0]*n #Aまでの合計時間
for i in range(1,n):
    if (i+1)%2==1: #終わり(3,5,7.. 1-indexed)で加算
        f[i]=f[i-1]+a[i]-a[i-1]
    else:
        f[i]=f[i-1]

for _ in range(int(input())):
    l,r=map(int, input().split())
    ll,rr=bisect_right(a,l)-1,bisect_right(a,r)-1
    fl=f[ll]+(l-a[ll] if ll%2==1 else 0) # 1個前まで＋その区間の途中まで
    fr=f[rr]+(r-a[rr] if rr%2==1 else 0)
    print(fr-fl)