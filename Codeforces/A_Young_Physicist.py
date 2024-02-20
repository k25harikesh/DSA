n = int(input())
L = []

for _ in range(n):
    L.append(list(map(int, input().split())))

cols = list(zip(*L))

idle = True
for col in cols:
    if sum(col) != 0:
        idle = False
        break

print('YES' if idle else 'NO')
