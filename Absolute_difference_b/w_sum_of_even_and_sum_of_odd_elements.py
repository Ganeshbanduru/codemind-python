num=int(input())
sum1=0
sum2=0
gan=list(map(int,input().split()))
for i in gan:
    if i%2==0:
        sum1+=i
    else:
        sum2+=i
print(abs(sum1-sum2))