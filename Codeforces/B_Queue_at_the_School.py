n, t = map(int, input().split())
queue = input()

for _ in range(t):
    new_queue = ''
    i = 0
    while i < n:
        if queue[i:i+2] == 'BG':
            new_queue += 'GB'
            i += 1
        else:
            new_queue += queue[i]
        i += 1

    queue = new_queue

print(queue)
