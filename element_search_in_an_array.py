num=int(input())
lst=list(map(int,input().split()))
m=int(input())
count=0
if m in lst:
    count+=1
if count==1:
    print("True")
else:
    print("False")