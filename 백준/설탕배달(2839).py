n = int(input())

count = 0

while (n > 0):
    namuji = n % 5
    if (namuji ==1 or namuji == 4):
        count += 2
        n -=6
    elif (namuji ==2 or namuji == 5):
        count += 1
        n -=3
    elif (namuji ==3):
        count += (n //5)
        n %=5
        count += 1
        n -=3
    elif (namuji == 0):
        count += (n //5)
        n %=5

if (n != 0):
    count = -1

print (count)