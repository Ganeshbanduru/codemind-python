n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
l=[]
for i in range(n):
    if(a>lst[i] or lst[i]>b):
        l.append(lst[i])
print(sum(l))
        