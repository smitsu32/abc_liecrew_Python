from sortedcontainers import SortedList

sl=SortedList([int(input())])
for i in range(int(input())):
    a,b=map(int,input().split())
    sl.add(a); sl.add(b)
    print(sl[i+1])