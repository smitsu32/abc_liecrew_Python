from atcoder.fenwicktree import FenwickTree

n,q=map(int, input().split())
INF=10**6+1

# 区間和→フェニック木
fw=FenwickTree(INF) #各値の個数
fw.add(0,n) 
h=[0]*n #各マスの高さ
offset=0

for i in range(q):
    t,x=map(int, input().split())
    if t==1:
        x-=1
        
        fw.add(h[x],-1)
        h[x]+=1
        fw.add(h[x],1)
        
        if fw.sum(0,offset+1)==0:
            offset+=1
        
    else:
        res=fw.sum(x+offset,INF)
        print(res)