n=int(input())
lst=list(map(int,input().split()))
m=int(input())
comp=0
if m in lst:
    comp+=1
if comp==1:
    print("True")
else:
    print("False")