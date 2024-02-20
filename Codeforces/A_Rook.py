left = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
right = ['1', '2', '3', '4', '5', '6', '7', '8']

tc = []
output = []

for i in range(int(input())):
    tc.append(input())

lft = tc[0][0]
rht = tc[0][1]

if lft in left:
    L = list((lft+'1', lft+'2', lft+'3', lft+'4', lft+'5', lft+'6',
                  lft+'7', lft+'8'))
    output.extend(L)
if rht in right:
    R = ('a'+rht, 'b'+rht, 'c'+rht, 'd'+rht, 'e'+rht,
                  'f'+rht, 'g'+rht, 'h'+rht)
    output.extend(R)

output = [elem for elem in output if elem not in tc]
print("\n".join(output))
