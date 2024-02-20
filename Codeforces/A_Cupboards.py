t = int(input())

List = []
Listleft = []
Listright = []

for _ in range(t):
    List += input().split()


for i in range(len(List)):
    if i % 2 == 0:
        numl = list(map(int, List[i]))
        Listleft.append(numl)
    else:
        numr = list(map(int, List[i]))
        Listright.append(numr)

Listleft = [item for sublist in Listleft for item in sublist]
Listright = [item for sublist in Listright for item in sublist]


if sum(Listleft) == 0 and sum(Listright) == 0:
    print(0)
elif sum(Listleft) > sum(Listright):
    print(min(t-sum(Listleft), sum(Listleft)) +
          min(t-sum(Listright), sum(Listright)))
else:
    print(min(t-sum(Listleft), sum(Listleft)) +
          min(t-sum(Listright), sum(Listright)))
