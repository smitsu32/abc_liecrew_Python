n=int(input())
l,r=1,n
while abs(r-l)>1:
    mid=(l+r)//2
    print('?',mid,flush=True)
    m=int(input())
    if m==1:
        r=mid
    else:
        l=mid
print('!',l)