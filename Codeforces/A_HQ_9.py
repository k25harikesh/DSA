l = input()
l2 = 'HQ9'

label = False

for i in range(len(l)):
    if l[i] in l2:
        label = True
        break

print('YES' if label else 'NO')
