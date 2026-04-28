import sys
sys.setrecursionlimit(10**6)

n=int(input())
a=list(map(int, input().split()))

g=[[] for i in range(n)]
for i in range(n-1):
    u,v=map(int, input().split())
    u-=1; v-=1
    g[u].append(v)
    g[v].append(u)

visited=[False]*n #累計で通った点
s=set() #今通った点
cnt=0 #重複数
ans=[0]*n #答え用
def dfs(i):
    global cnt
    
    visited[i]=True
    f=False # ifがどっちか
    
    # 侵入
    if a[i] in s:
        cnt+=1 # 既にあったら+1
        f=True 
    else:
        s.add(a[i]) #ないとき追加
    
    if cnt>0: #answer
        ans[i]=1
    
    for ni in g[i]:
        if not visited[ni]:
            dfs(ni)
    
    # 退出
    if f:
        cnt-=1 # もとにもどす
    else:
        s.remove(a[i]) # 戻って重複がなくなったとき削除

dfs(0)

for i in range(n):
    if ans[i]==1:
        print('Yes')
    else:
        print('No')