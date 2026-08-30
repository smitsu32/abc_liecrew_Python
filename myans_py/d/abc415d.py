n,m=map(int, input().split())
abc=[]
for i in range(m):
    a,b=map(int, input().split())
    abc.append([a-b,a,b]) #a-bで昇順ソート
abc.sort()

ans=0
for c,a,b in abc:
    x=max((n-a)//c+1,0) # 1回ごとにc個減る (n-a)//c+1回 (+1は割り切れる分)
    ans+=x
    n-=x*c
print(ans)