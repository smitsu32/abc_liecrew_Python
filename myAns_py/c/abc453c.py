from time import time
n=int(input())
l=list(map(int, input().split()))
mx=0
for bit in range(2**n):
    cnt=0
    x=0.5
    for i in range(n):
        if (bit>>i)&1:
            nx=x+l[i]
        else:
            nx=x-l[i]
        
        if nx*x<0:
            cnt+=1
        x=nx
    mx=max(mx,cnt)
print(mx)