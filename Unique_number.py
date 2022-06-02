n=int(input())
n=str(n)
n=list(n)
b=[]
for i in n:
    if n.count(i)<=1:
        b.append(i)
if len(n)==len(b):
    print("Unique Number")
else:
    print("Not Unique Number")