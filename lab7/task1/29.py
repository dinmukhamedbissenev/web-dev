a = int(input())
ar = list(map(int, input().split()))
for i in range(a):
    if i % 2 == 0:
        print(ar[i], end = ' ')