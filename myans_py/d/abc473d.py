n,k=map(int, input().split())

def dfs(cnt,now,a): 
    if cnt==n: #最終indexなら結果を出力、終了
        if (k-now)%n==0:
            a[cnt-1]=(k-now)//n
            print(*a)
        return 
    i=0
    while k-now>=cnt*i: # 割った結果が0以上
        a[cnt-1]=i
        dfs(cnt+1,now+cnt*i,a)
        i+=1
dfs(1,0,[0]*n)