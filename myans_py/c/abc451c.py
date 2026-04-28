from sortedcontainers import SortedList

Q=int(input())
l=SortedList()
idx=0
cnt=0

for i in range(Q):
    q,h=map(int, input().split())
    if q==1:
        l.add(h)
        cnt+=1
    else:
        idx=l.bisect_right(h)
        del l[:idx]
    print(len(l))