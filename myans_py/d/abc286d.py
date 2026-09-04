n,x=map(int, input().split())
dp=[[False]*(x+1) for i in range(n+1)] #i種類でj円達成できるか
dp[0][0]=True

for i in range(n):
    a,b=map(int, input().split())
    for j in range(x+1): #今まででOKの金額
        if not dp[i][j]:
            continue
        for k in range(b+1): 
            if j+k*a<=x:
                dp[i+1][j+k*a]=True

print('Yes' if dp[-1][-1] else 'No')