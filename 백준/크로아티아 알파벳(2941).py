a = input()
croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croa:
    a = a.replace(i, 'a')

print(len(a))