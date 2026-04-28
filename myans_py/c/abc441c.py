n,k,x=map(int, input().split())
a=list(map(int, input().split()))

a.sort(reverse=True)
ans=n-k # 個数
now=0 # 今のml
for i in range(n-k,n): # 最悪ケースを確認
    ans+=1
    now+=a[i]
    if now>=x:
        break

if now<x: #最悪ケースでx mlに満たないとき
    print(-1)
else:
    print(ans)