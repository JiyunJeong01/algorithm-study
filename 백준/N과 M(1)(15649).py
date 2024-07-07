import itertools

N, M = map(int,input().split())
arr = [i+1 for i in range(N)]
nPr = itertools.permutations(arr, M)
for perm in nPr:
    print(' '.join(map(str, perm)))