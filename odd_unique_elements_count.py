p=int(input())
q=list(map(int,input().split()))
o=[]
i=[]
for r in q:
    if r not in o:
        o.append(r)
for y in o:
    if y%2!=0:
        i.append(y)
print(len(i))
    