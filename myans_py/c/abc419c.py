s=input()
e=['red','blue','green']
a=['SSS','FFF','MMM']

for i in range(3):
    if e[i]==s:
        print(a[i])
        exit()
print('Unknown')