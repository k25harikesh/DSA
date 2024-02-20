m, d = list(map(int, input().split()))
Y, M, D = list(map(int, input().split()))

D += 1

if D > d:
    D = 1
    M += 1
if M > m:
    M = 1
    Y += 1

print(Y, M, D)
