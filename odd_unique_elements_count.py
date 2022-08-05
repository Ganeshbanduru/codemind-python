n=int(input())
q=list(map(int,input().split()))
o=[]
l=[]
for i in q:
    if i%2!=0:
        o.append(i)
for x in o:
    if x not in l:
        l.append(x)
print(len(l))