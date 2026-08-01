from bisect import bisect_left,bisect_right

n=int(input())
s=input()

x=[0]*(n+1)
now=0
for i in range(n):
    if s[i]=='x':
        now+=1
    x[i+1]=now

for i in range(n):
    if bisect_left(x,i+1)<=n:
        print(bisect_left(x,i+1))
    else:
        print(n)