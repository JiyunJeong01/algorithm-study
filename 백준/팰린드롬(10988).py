a = input()
pnp = 1
for i in range (len(a)//2):
    if (a[i] == (a[-(i+1)])):
        pass
    else:
        pnp = 0
        break
print (pnp)