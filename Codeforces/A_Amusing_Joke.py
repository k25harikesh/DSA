# nm1 = input()
# nm2 = input()
# nm3 = input()
# nm = nm1+nm2

# check_arr1 = all(char in nm3 for char in nm)

ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

guest_host = input() + input()
pile = input()

found = True
for letter in ascii_uppercase:
    if guest_host.count(letter) != pile.count(letter):
        found = False

print('YES' if found else 'NO')
