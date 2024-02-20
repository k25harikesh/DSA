n = int(input())
count = 0
ops_list = []

for i in range(n):
    ops_list.extend(input().split("X"))

for op in ops_list:
    if op == '++':
        count += 1
    elif op == '--':
        count -= 1

print(count)
