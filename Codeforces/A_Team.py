n = int(input())
matrix = []
count = 0

for i in range(n):
    matrix.append(list(map(int, input().split())))

# mat_t = list(zip(*matrix))

for i in range(n):
    if sum(matrix[i]) > 1:
        count += 1
print(count)
