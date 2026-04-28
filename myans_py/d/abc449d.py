l,r,d,u=map(int, input().split())

# |x|>|y|
ans=0
for x in range(l,r+1):
    if x%2==0:
        # max(-|x|+1,D) <= y <= min(|x|-1,U)
        D=max(-(abs(x)-1),d) # -|x|<y<|x| 
        U=min(abs(x)-1,u) 
        ans+=max(U-D+1,0)

# |x|<=|y|
for y in range(d,u+1):
    if y%2==0:
        # max(-|y|,l) <= x <= min(|y|,r)
        L=max(l,-abs(y)) # -|x|<=y<|x|
        R=min(abs(y),r)
        ans+=max(R-L+1,0)

print(ans)