from collections import defaultdict

n=int(input())
a=list(map(int, input().split()))

# min(i,j,k)=jのjについて、適切なi,kをカウントする関数
def f(lis):
    ans=0
    d=defaultdict(int)
    for i in lis:
        if i%5==0:
            ans+=d[i//5*7]*d[i//5*3] #何通りか
        d[i]+=1
    return ans

res=0
# min(i,j,k)=jのとき
res+=f(a)
# max(i,j,k)=jのとき（右端から見る）
res+=f(a[::-1])

print(res)