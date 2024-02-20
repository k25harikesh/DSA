a = input()
b = input()

final = ''

for i in range(len(a)):
    if a[i] != b[i]:
        final += '1'
    else:
        final += '0'

print(final)
