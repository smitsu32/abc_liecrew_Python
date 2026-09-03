n=int(input())
s=input()

a,b=[],[] #a:答え　b:(の個数
for i in range(n):
    if s[i]=='(':
        b.append(len(a)) #(以降の文字数
        a.append(s[i])
    elif s[i]==')':
        if b:
            del a[b.pop():] #最後の(以降を削除
        else:
            a.append(s[i])
    else:
        a.append(s[i])
print(*a,sep='')