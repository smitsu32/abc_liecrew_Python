n,m=map(int, input().split())
ab=[list(map(int, input().split())) for i in range(m)]

def check(i,j): # i,jペアがありえるか
    for k in range(m):
        if i not in ab[k] and j not in ab[k]:
            return False
    
    return True

ans=0
for ab0 in [ab[0][0],ab[0][1]]: # ペアの１人目決定
    f=False # 2人目がいるか
    for i in range(m):
        if ab0 not in ab[i]: # ペアの２人目決定
            if check(ab0,ab[i][0]):
                ans+=1
            if check(ab0,ab[i][1]):
                ans+=1
            
            f=True
            break
    
    if not f: # 1人でいいなら他全員OK
        ans+=n-1

if check(ab[0][0],ab[0][1]): # 1試合目の人がどっちもOKなとき
    ans-=1

print(ans)