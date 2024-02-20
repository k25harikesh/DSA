year = int(input())
new_year = year

beautiful_yr = False

while not beautiful_yr:
    new_year += 1
    if len(set(str(new_year))) == 4:
        beautiful_yr = True

print(new_year)
