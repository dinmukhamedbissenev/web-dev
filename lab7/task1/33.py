n = int(input())

a = list(map(int, input().split()))
s = 0
for i in range(n - 1):
    if(a[i - 1] > 0 and a[i] > 0 or a[i - 1] < 0 and a[i ] < 0):
        s += 1

    
if(s >= 2):
    print('YES')
else:
    print('NO')