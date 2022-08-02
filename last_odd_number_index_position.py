q=int(input())
qpm=list(map(int,input().split()))
for i in range(q-1,-1,-1):
    if qpm[i]%2!=0:
        print(i)
        break