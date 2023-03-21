a = int(input())

b = int(input())
for i in range(a, b+ 1):
    if(i % ( i ** 0.5) == 0):
        print(i, end=' ')