k, n = map(int, input().split())
lines = []
for i in range(k):
    lines.append(int(input()))

low = 1
high = max(lines)

while low <= high:
    mid = (low + high) // 2
    count = 0
    
    for line in lines:
        count += line // mid
    
    if count >= n:
        low = mid + 1 
    else:
        high = mid - 1

print(high)