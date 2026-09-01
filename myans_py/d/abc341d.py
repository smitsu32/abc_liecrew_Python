n,m,k=map(int, input().split())

def gcd(x,y):
    while abs(x-y)>0 and y%x!=0:
        if x>y: x,y=y,x
        y%=x
    return x

# N と M のうち ちょうど一方のみ で割り切れる数の個数を二分探索
g=n*m//gcd(n,m)
l,r=0,10**18
while abs(l-r)>1:
    mid=(l+r)//2
    if mid//n + mid//m - 2*(mid//g)>=k: #(n,mの約数)-(n,mの公約数)
        r=mid
    else:
        l=mid

print(r)