a1 = input().lower()
a2 = input().lower()

if a1 == a2:
    print(0)

else:
    print('-1' if (a1 < a2) else '1')
