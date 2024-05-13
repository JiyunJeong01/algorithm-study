a = int(input())
for i in range(2*a-1):
    if (i <= (a-1)):
        print((" ") * (a-(i+1)) + ("*") * (1 + i*2))
    else:
        print((" ") * (i+1-a) + ("*") * (1 + ((2*a-2)-i)*2))