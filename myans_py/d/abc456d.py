s=input()
n=len(s)
MOD=998244353

# 終わりがa,b,cの連続しない文字数
a,b,c=0,0,0

for i in range(n):
    if s[i]=='a':
        a=(a+1+b+c)%MOD #終わりがa以外のものを+1('aa'のときはa=1に)
    elif s[i]=='b':
        b=(a+b+1+c)%MOD
    else:
        c=(a+b+c+1)%MOD

print((a+b+c)%MOD)