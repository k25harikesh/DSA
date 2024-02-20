n = int(input())
List = list(map(int, input().split()))

result = round(sum(List) / n, 12)

print('{:.12f}'.format(result))
