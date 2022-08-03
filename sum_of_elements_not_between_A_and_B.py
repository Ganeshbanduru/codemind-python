n=int(input())
gani=list(map(int,input().split()))
q,p=map(int,input().split())
e=[]
for y in range(n):
    if q>gani[y] or gani[y]>p:
        e.append(gani[y])
print(sum(e))