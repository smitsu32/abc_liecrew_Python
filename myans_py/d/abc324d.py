n=int(input())
s=list(input())
s.sort()

ans,i=0,0
while True: #平方根を順番に探索
    j=list(str(i**2))
    j.sort()
    if len(j)>n:
        break
    j=['0']*(n-len(j))+j #0が足りないならそろえる
    if j==s:
        ans+=1
    i+=1
print(ans)