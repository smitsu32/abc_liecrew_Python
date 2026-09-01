n=int(input())
a=list(map(int, input().split()))
MOD=998244353

p=[pow(10,len(str(i)),MOD) for i in a] #各項が下となったときの0の数
ans=0
s=sum(p) #下の数の桁を全部足した
for i in range(n):
    s-=p[i] #i番目が下を考えない
    ans=(ans + a[i]*s + i*a[i])%MOD #a[i]が上の時＋下の時
print(ans)