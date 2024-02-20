n = int(input())
L = list(map(int, input().split()))

count = -2
min = float('inf')
max = float('-inf')

for i in range(n):
    if L[i] > max:
        max = L[i]
        count += 1
    if L[i] < min:
        min = L[i]
        count += 1

print(count)
