n,q=map(int, input().split())

# a:各マスのブロック数、b:各ブロック数のマスの数
a,b=[0]*(n+1),[0]*(q+1)
offset=0
for i in range(q):
    t,x=map(int, input().split())
    if t==1:
        a[x]+=1
        b[a[x]]+=1
        if b[a[x]]==n:
            offset=a[x]
    
    else:
        if x+offset<=q: #リスト内なら
            print(b[x+offset]) #何個か出力（N個の段はパス）
        else:
            print(0)