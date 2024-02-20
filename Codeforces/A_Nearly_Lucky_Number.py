num = str(input())

count = 0

for i in num:
    if i == '4' or i == '7':
        count += 1

label = True

count = str(count)

for i in count:
    if i not in ['4', '7']:
        label = False
        break

print('YES' if label else 'NO')
