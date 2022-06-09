num=int(input())
even_sum=0
odd_sum=0
lst=list(map(int,input().split()))
for i in range(num):
    if i%2==0:
        even_sum+=lst[i]
    else:
        odd_sum+=lst[i]
print(abs(even_sum-odd_sum))