n = int(input())
jibang = list(map(int,input().split()))
total = int(input())

start, end = 1, max(jibang)

while start <= end:
    mid = (start+end) //2

    #총 배분한 양
    log = 0
    for i in jibang:
        if i >=mid:
            log += mid
        else:
            log += i
    
    if log <= total:
        start = mid + 1
    else:
        end = mid - 1
print (end)