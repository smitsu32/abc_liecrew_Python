for i in range(int(input())):
    n,h=map(int, input().split())
    tlu=[list(map(int, input().split())) for i in range(n)]
    pt,pl,pu=0,h,h
    f=True
    for t,l,u in tlu:
        dt=t-pt
        nl,nu=max(1,pl-dt),pu+dt # 0以下NG
        if nu<l or nl>u:
            f=False
            break
        else:
            pt,pl,pu=t,max(nl,l),min(nu,u)
    
    if f: print('Yes')
    else: print('No')