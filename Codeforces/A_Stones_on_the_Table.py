n = int(input())
series = input()

count = 0

for i in range(1, n):
    if series[i] == series[i-1]:
        count += 1

print(count)
