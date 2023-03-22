a = int(input())
ar = list(map(int, input().split()))
for i in range(a):
    if(ar[i] % 2 == 0):
        print(ar[i], end=' ')