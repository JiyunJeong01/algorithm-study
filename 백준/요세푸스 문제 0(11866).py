num, interval = map(int,input().split())

queue = []
for i in range(num):
    queue.append(i+1)

check = 1
solve = []
while len(queue) != 0:
    if (check % interval) ==0:
        solve.append(queue.pop(0))
    else:
        queue.append(queue.pop(0))
    check += 1

lst_str = str(solve)[1:-1]
print("<"+lst_str+">")