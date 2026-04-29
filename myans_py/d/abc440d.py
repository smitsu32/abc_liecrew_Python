from bisect import bisect_left

n,q=map(int, input().split())
a=list(map(int, input().split()))
a.sort()

for i in range(q):
    x,y=map(int, input().split())
    
    s=bisect_left(a,x)
    # 答えがあるaの区間インデックスをかえす
    ok=n #max
    ng=s-1 #min
    while ok-ng>1:
        mid=(ok+ng)//2
        # a[mid]までの空地数がy以上か?
        # ぜんぶ - a
        if (a[mid]-(x-1))-(mid-(s-1))>=y:
            ok=mid
        else:
            ng=mid
        
    # xからy番目＋通行止めの数
    ans=x+(y-1)+(ok-s)
    print(ans)