q=int(input())
zzz=list(map(int,input().split()))
count=0
for m in range(1,q-1):
    if zzz[m-1]%2==0 and zzz[m+1]%2!=0 or zzz[m-1]%2!=0 and zzz[m+1]%2==0:
        count+=1
print(count)