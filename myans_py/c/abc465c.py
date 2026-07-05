from collections import deque

n=int(input())
s=input()

f=True
d=deque()
# 反転中なら前に、じゃないなら後ろに追加
for i in range(n):
    if f:
        d.append(i+1)
    else:
        d.appendleft(i+1)
    
    if s[i]=='o':
        f^=True
# 最後だけ反転できてない
if not f:
    d.reverse()

print(*d)