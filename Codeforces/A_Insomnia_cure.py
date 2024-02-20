List = []

for i in range(5):
    List.append(input())

List2 = [int(k) for k in List]

k, l, m, n, d = List2

count = 0

for i in range(1, d+1):

    divisibleByk = i % k == 0
    divisibleByl = i % l == 0
    divisibleBym = i % m == 0
    divisibleByn = i % n == 0

    if (divisibleByk) or (divisibleByl) or (divisibleBym) or (divisibleByn):
        count += 1

print(count)
