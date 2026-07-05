for _ in range(int(input())):
    a,b,c=map(int, input().split())
    ans=min(min(a,c),(a+b+c)//3)
    print(ans)