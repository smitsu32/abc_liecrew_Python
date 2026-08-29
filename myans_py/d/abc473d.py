n,k=map(int, input().split())

d=[[k,n,[]]]
ans=[]
while d:
    now,cnt,ansi=d.pop()
    if cnt==1:
        ansi.append(now)
        ans.append(ansi[::-1])
    else:
        i=0
        while now>=cnt*i:
            d.append([now-cnt*i,cnt-1,ansi+[i]])
            i+=1

ans.sort()
for l in ans:
    print(*l)