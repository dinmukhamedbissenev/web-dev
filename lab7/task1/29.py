a = int(input())
ar = []
for i in range(a):
    ar.append(int(input()))

print(i % 2 == 0 for i in range(len(ar)))