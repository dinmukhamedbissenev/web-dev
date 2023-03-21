a = input()
a = a[::-1]
s = 0
for i in range(len(a)):
    s += 2 ** i * int(a[i])

print(s)