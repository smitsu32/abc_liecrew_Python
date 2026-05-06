t=int(input())
for i in range(t):
    n=int(input())
    wp=[]
    psum=0
    for i in range(n):
        w,p=map(int, input().split())
        wp.append([w,p])
        psum+=p
    wp.sort(key=lambda x:x[0]+x[1])
    
    cnt=0 # 重さ+引く力
    for i in range(n):
        cnt+=wp[i][0]+wp[i][1]
        if cnt>psum: # cntで徐々にpも増える
            print(i)
            break