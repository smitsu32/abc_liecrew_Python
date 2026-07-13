n=int(input())

cnt=0
r=1 #距離1未満が確定している点
# 尺取り O(2N-2)
for i in range(1,n):
    r=max(r,i)
    while r<n:
        print('?',i,r+1,flush=True)
        if input()=='Yes':
            r+=1
        else:
            break
    cnt+=r-i

print('!',cnt,flush=True)