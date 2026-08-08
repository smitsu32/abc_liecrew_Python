n,q=map(int, input().split())
l=[0]*n
ex=[]
xor=0
for _ in range(q):
    qu=list(map(int, input().split()))
    if qu[0]==1:
        x=qu[1]-1
        
        xor^=l[x] #古いのを消す
        l[x]+=1
        if l[x]==1:
            ex.append(x)
        xor^=l[x] #新しいのを足す　^= ^= ->元の値
    else:
        nex=[]
        for i in ex:
            xor^=l[i]
            l[i]=max(l[i]-1,0)
            xor^=l[i]
            if l[i]!=0:
                nex.append(i)
        ex=nex
        
    print(xor)