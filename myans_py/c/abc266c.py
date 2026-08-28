a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=list(map(int,input().split()))

def j(a,b,c): #反時計回り
    if (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])>0:
        return True
    else:
        return False

if j(a,b,d) and j(b,c,a) and j(c,d,b) and j(d,a,c):
    print('Yes')
else:
    print('No')