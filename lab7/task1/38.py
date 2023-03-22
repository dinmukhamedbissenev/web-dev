def xor(x, y):
    if x + y== 1:
        print(1)
    else:
        print(0)

x, y = map(int, input().split())
xor(x, y)