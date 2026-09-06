for _ in range(int(input())):
    n=int(input())
    abc=[]
    for i in range(n):
        a,b=map(int, input().split())
        abc.append([a,b,a-b])
    abc.sort(key=lambda x:-x[2])
    d=[0]
    for i in range(n):
        d.append(d[-1]+abc[i][2])
    
    sm=sum(abc[i][0] for i in range(n))
    mn=min(abc[i][0] for i in range(n))
    ans=sm
    for i in range(n+1): #Bを買った個数
        if i-(n-i)>0: #クーポンの不足枚数=mn円でこれだけ買う
            ans=min(ans,sm-d[i]+mn*(i-(n-i)))
        else:
            ans=min(ans,sm-d[i])
    print(ans)