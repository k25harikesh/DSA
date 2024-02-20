List = map(int, input().split())
n, k, l, c, d, p, nl, np = List

total_lime_slices = c*d
milliliters_of_the_drink = k*l

print(min(k*l//nl, c*d, p//np)//n)
