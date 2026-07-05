from bisect import bisect_left,bisect_right

n=int(input())
hl=[list(map(int, input().split())) for i in range(n)]
q=int(input())
t=list(map(int, input().split()))

h,l=[],[]
mx=-1
for i in range(n-1,-1,-1):
    if mx<hl[i][0]:
        mx=hl[i][0]
        h.append(hl[i][0])
        l.append(hl[i][1])
h=h[::-1]; l=l[::-1]

for i in range(q):
    print(h[bisect_right(l,t[i])])