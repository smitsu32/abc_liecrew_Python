from math import gcd

def g(a,b,c): # ax+by+c=0 (a>=0,(a=0ならb>0)の共通形にする関数)
    gg=gcd(a,gcd(b,c))
    na,nb,nc=a//gg,b//gg,c//gg # 最大公約数で割る
    if na<0:
        na,nb,nc=-na,-nb,-nc
    elif na==0 and nb<0:
        nb,nc=-nb,-nc
    return na,nb,nc

for i in range(int(input())):
    px,py,qx,qy,rx,ry,sx,sy=map(int, input().split())
    #直線pqの式 (x-px)^2 +(y-py)^2=(x-qx)^2 +(y-qy)^2を変形
    a,b,c=2*(px-qx),2*(py-qy),qx**2+qy**2-px**2-py**2
    d,e,f=2*(rx-sx),2*(ry-sy),sx**2+sy**2-rx**2-ry**2
    
    na,nb,nc=g(a,b,c)
    nd,ne,nf=g(d,e,f)
    # 平行でない、標準化した垂直二等分線が同一(２直線が重なる)
    if a*e-b*d!=0 or (na==nd and nb==ne and nc==nf):
        print('Yes')
    else:
        print('No')