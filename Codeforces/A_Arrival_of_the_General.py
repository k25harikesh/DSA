n = int(input())
List = list(map(int, input().split()))

max_height_at = List.index(max(List))
min_height_at = len(List) - List[::-1].index(min(List)) - 1
# using array reversing to find the last index of min elem

steps = 0
steps += max_height_at

if max_height_at > min_height_at:
    steps += n-(min_height_at+1)-1
else:
    steps += n-(min_height_at+1)


print(steps)
