n=int(input())
zzz=list(map(int,input().split()))
a,b=map(int,input().split())
k=0
count=[]
for w in range(n):
    if a>zzz[w] or b<zzz[w]:
        count.append(zzz[w])
        k=1
if k==0:
    print("-1")
else:
    print(*count)
        