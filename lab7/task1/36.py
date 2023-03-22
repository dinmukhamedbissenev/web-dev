def min(a, b, c, d):
    a = [a, b, c , d]
    a.sort()
    print(a[0])

a, b, c, d = map(int, input().split())
min(a,b,c,d)