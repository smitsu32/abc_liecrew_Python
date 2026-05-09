n,k=map(int, input().split())
a=list(map(int, input().split()))

# 答えを二分探索したい
# 最悪:A=[1],K=10**18 -> X=2*10**18+1
ok,ng=0,10**24
while abs(ok-ng)>1:
    mid=(ok+ng)//2
    cnt=0
    for i in range(n):
        # (x-a[i]-1)//i+1回増やせばよい 3->6->9->12 (x:11)
        # 3->4のとき数えたいので最後に+1
        # 3->6を1回とするためカッコ内-1
        cnt+=max(0,(mid-a[i]-1)//(i+1)+1)
    
    if cnt<=k: #ok
        ok=mid
    else:
        ng=mid

print(ok)