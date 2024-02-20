n, m = list(map(int, input().split()))
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

indexOfn = primes.index(n)
if m in primes:
    indexOfm = primes.index(m)
else:
    indexOfm = -23

print('YES' if indexOfm == indexOfn+1 else 'NO')
