t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    x=list(map(int, input().split()))
    y=list(map(int, input().split()))
    
    sn,rn=[0]*n,[0]*n
    if s[0]=='S':
        rn[0]=-x[0]
    else:
        sn[0]=-x[0]
    
    for i in range(1,n):
        if s[i]=='S':
            sn[i]=max(sn[i-1],rn[i-1]+y[i-1]) # 昨日(晴or雨)今日晴れ
            rn[i]=max(rn[i-1],sn[i-1])-x[i] #晴れ→雨に強制変更
        else:
            rn[i]=max(sn[i-1],rn[i-1]) #雨
            sn[i]=max(sn[i-1],rn[i-1]+y[i-1])-x[i] #雨→晴れに
    
    print(max(sn[-1],rn[-1]))