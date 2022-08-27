n=int(input())
lst=list(map(int,input().split()))
avg=sum(lst)//len(lst)
if avg in lst:
    print("True")
else:
    print("False")