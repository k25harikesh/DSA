num_of_eggs, pack_6, pack_8, pack_12 = list(map(int, input().split()))

cost = 0

pckt6 = num_of_eggs / 6
pckt8 = num_of_eggs / 8
pckt12 = num_of_eggs / 12

p6ph = num_of_eggs/pack_6
p8ph = num_of_eggs/pack_8
p12ph = num_of_eggs/pack_12


print(pckt6*p6ph)
print(pckt8*p8ph)
print(pckt12*p12ph)

# print(p6ph)
# print(p8ph)
# print(p12ph)

# print(pckt6)
# print(pckt8)
# print(pckt12)
