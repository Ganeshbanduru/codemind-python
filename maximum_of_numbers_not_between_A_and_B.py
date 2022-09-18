n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
l=[]
s=0
for i in range(len(lst)):
    if(lst[i]<a or b<lst[i]):
        l.append(lst[i])
        s=1
if(s==0):
    print("-1")
else:
    print(max(l))